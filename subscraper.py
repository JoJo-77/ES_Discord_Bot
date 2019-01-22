from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class Scraper: 

	def __init__(self,url):
		self.url = url
		self.headerend = 41
		self.chromedriver = "./chromedriver"
		self.driver = webdriver.Chrome(chromedriver)
		self.actions = ActionChains(driver)
		self.workerdict = {}

	def get_web_text():
		return driver.find_element_by_tag_name("body").text.split("\n")[self.headerend:]

	def clean_web_text():
		schedule = get_web_text()
		schedule.remove("ES Support Assistants")
		schedule.remove("ES Student Operations")
		for s in sorted(range(len(schedule)),reverse = True):
			if schedule[s] == '':
				del schedule[s]
		workers = [schedule[x] for x in range(len(schedule)) if x % 2 ==0]
		shifts = [schedule[x] for x in range(len(schedule)) if x % 2 !=0]
		make_dict(workers,shifts)

	def make_dict(workers,shifts):
		for x in range(len(workers)):
			if workers[x] not in self.workerdict.keys():
				self.workerdict[workers[x]] = [shifts[x]]
			elif workers[x] in self.workerdict.keys() and shifts[x] not in self.workerdict[workers[x]]:
				self.workerdict[workers[x]].append(shifts[x])

	def print_dict():
		for worker in workerdict.keys():
			print(worker,workerdict[worker])
			print('\n')

	def close():
		self.driver.close()

