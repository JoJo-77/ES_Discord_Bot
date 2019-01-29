from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class Scraper: 

	def __init__(self,url):
		self.url = url
		self.headerend = 41
		self.driver = webdriver.Chrome("./chromedriver")
		self.actions = ActionChains(self.driver)
		self.workerdict = {}
		self.driver.get(self.url)
		time.sleep(4)

	def get_web_text(self):
		return self.driver.find_element_by_tag_name("body").text.split("\n")

	def scrape(self):
		schedule = self.get_web_text()[self.headerend:]
		schedule.remove("ES Support Assistants")
		schedule.remove("ES Student Operations")
		for s in sorted(range(len(schedule)),reverse = True):
			if schedule[s] == '':
				del schedule[s]
		workers = [schedule[x] for x in range(len(schedule)) if x % 2 ==0]
		shifts = [schedule[x] for x in range(len(schedule)) if x % 2 !=0]
		self.make_dict(workers,shifts)

	def make_dict(self,workers,shifts):
		for x in range(len(workers)):
			if workers[x] not in self.workerdict.keys():
				self.workerdict[workers[x]] = [shifts[x]]
			elif workers[x] in self.workerdict.keys() and shifts[x] not in self.workerdict[workers[x]]:
				self.workerdict[workers[x]].append(shifts[x])

	def print_dict(self):
		for worker in self.workerdict.keys():
			#print(worker,self.workerdict[worker])
			#print('\n')
			self.print_worker(worker)

	def sort_shifts(self):
		ret = 0
		shift = self.get_shift().title()
		for worker in self.workerdict.keys():
			for item in self.workerdict[worker]:
				if shift in item:
					print(worker, self.workerdict[worker])
					ret = 1
			else:
				continue 
		return ret

	def print_worker(self,worker):
		ret = (worker + ": ")
		for shift in self.workerdict[worker]:
			ret + shift + ", "
		print(ret)

	def get_shift(self):
		inp = input("What shift do you want to see:\n")
		return inp

	def close(self):
		self.driver.close()

'''
Testing OOP
'''
def main():
	scraper = Scraper("https://account.subitup.com/public/?5t7i0fpakJA%3d#byTimeDay")
	scraper.scrape()
	scraper.print_dict()
	scraper.close()
	retval = scraper.sort_shifts()
	while (retval is not 0):
		retval = scraper.sort_shifts()





if __name__ == "__main__":
	main()

