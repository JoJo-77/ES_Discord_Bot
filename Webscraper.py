from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

'''
Initialization of file paths, optional output, and constants
'''
chromedriver = "./chromedriver"
#output = open("out.txt","w")
endofheaders = 41
driver = webdriver.Chrome(chromedriver)
actions = ActionChains(driver)
driver.get("https://account.subitup.com/public/?5t7i0fpakJA%3d#byTimeDay")
time.sleep(4)

'''
Website text scraping and cleaning up
Grabs all text and splits it at every new line, 
which gives us a list of alternating workers and shifts.
It then removes all titles and any unnecessary characters.
'''

fullschedule = driver.find_element_by_tag_name("body").text.split("\n")[endofheaders:]
fullschedule.remove("ES Support Assistants")
fullschedule.remove("ES Student Operations")
for s in sorted(range(len(fullschedule)),reverse = True):
	if fullschedule[s] == '':
		del fullschedule[s]

'''
Separates sorted text into workers and shifts.
Depends on list being correctly created above with alternating names and shifts.
'''
workers = [fullschedule[x] for x in range(len(fullschedule)) if x % 2 ==0]
shifts = [fullschedule[x] for x in range(len(fullschedule)) if x % 2 !=0]

'''
Creates a dictionary paring each worker to all of their shifts
This way we avoid having multiple entries for someone working more than one shift
'''
workerdict = {}
i = 0
for x in range(len(workers)):
	if workers[x] not in workerdict.keys():
		workerdict[workers[x]] = [shifts[x]]
	elif workers[x] in workerdict.keys() and shifts[x] not in workerdict[workers[x]]:
		workerdict[workers[x]].append(shifts[x])

'''
Prints dictionary of workers in readable format
'''

for worker in workerdict.keys():
	print(worker,workerdict[worker])
	print('\n')
driver.close()