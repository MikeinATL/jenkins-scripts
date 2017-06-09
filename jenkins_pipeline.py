#!/usr/bin/python3
"""
This module executes against Jenkins to get the pipeline PNG under Blue Ocean.
The script is created because of the lack of plugins/methods to get the PNG images

Example:

	$ chmod 775 jenkins_pipeline.py
        $ ./jenkins_pipeline.py

Todo:
    * Change Jenkins user/password
    * Change QA_Name to put the project to monitor
    * Change branch to monitor (QA_BUILD)

"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
from PIL import Image

QA_NAME = 'SMPP'
QA_BUILD = 'master'
JENKINSUSER = 'jenkins'
JENKINSPASSWORD = 'jenkins'
DELAY = 3

def main():
	""" Main Function"""
	chromedriver = '/usr/lib/chromium-browser/chromedriver'
	chrome_options = Options()
	chrome_options.add_argument("--headless")
	browser = webdriver.Chrome(chromedriver)
	browser.get('http://localhost:8080')
	browser.find_element_by_id("j_username").send_keys(JENKINSUSER)
	browser.find_element_by_name("j_password").send_keys(JENKINSPASSWORD)

	browser.find_element_by_name("Submit").click()
	browser.find_element_by_id("open-blueocean-in-context").click()
	time.sleep(DELAY)
	browser.find_element_by_link_text(QA_NAME).click()
	time.sleep(DELAY)

	initialvalue = 0
	for i in browser.find_elements_by_link_text(QA_BUILD):
		split = i.get_attribute('href').split('/')
		if initialvalue < int(split[9]):
			final_url = i.get_attribute('href')
			initialvalue = int(split[9])

	browser.get(final_url)
	time.sleep(DELAY)
	qa_pipeline = browser.find_element_by_xpath('//*[@id="outer"]/div/span/div/div/div/div[1]/div/div/div')
	browser.save_screenshot('/tmp/jenkins.png')
	image_start = Image.open('/tmp/jenkins.png')
	location = qa_pipeline.location
	size = qa_pipeline.size

	left = location['x']
	top = location['y']
	right = location['x'] + size['width']
	bottom = location['y'] + size['height']

	image_start.crop((left, top, right, bottom)).save('/tmp/jenkins.png')

	browser.close()

if __name__ == '__main__':
	display = Display(visible=0, size=(800, 600))
	display.start()
	main()
