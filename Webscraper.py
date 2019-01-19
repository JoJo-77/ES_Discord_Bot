from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

chromedriver = "./chromedriver"
output = open("out.txt","w")
endofheaders = 41
driver = webdriver.Chrome(chromedriver)
actions = ActionChains(driver)
driver.get("https://account.subitup.com/public/?5t7i0fpakJA%3d#byTimeDay")
time.sleep(4)
el = driver.find_element_by_tag_name("body")

fullschedule = el.text.split("\n")[endofheaders:]
fullschedule.remove("ES Support Assistants")
fullschedule.remove("ES Student Operations")

workers = []
shifts = []

for s in sorted(range(len(fullschedule)),reverse = True):
	if fullschedule[s] == '':
		del fullschedule[s]
for s in range(len(fullschedule)):
	if s % 2 == 0:
		workers.append(fullschedule[s])
	else:
		shifts.append(fullschedule[s])
#print(workers)
#print(shifts)

workerdict = {}
i = 0
for x in range(len(workers)):
	if workers[x] not in workerdict.keys():
		workerdict[workers[x]] = [shifts[x]]
	elif workers[x] in workerdict.keys() and shifts[x] not in workerdict[workers[x]]:
		workerdict[workers[x]].append(shifts[x])

for worker in workerdict.keys():
	print(worker,workerdict[worker])
	print('\n')
driver.close()