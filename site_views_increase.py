#This is a program to increase the views of a site. This is purely an experiment.
#I have considered using urllib2 so send ping requests instead of selenium for opening the browser, but in my tests the views did not count.
#I have used the chrome browser in a mac environment you may have different browser or environment check the chrome driver documentation.

from selenium import webdriver
import time
import random

#find out your chrome version and download the driver to the "/usr/local/bin" folder.
#you can get the driver at "https://chromedriver.chromium.org/downloads"

#chrome is opened using the driver
driver = webdriver.Chrome('/usr/local/bin/chromedriver')

#enter these values
times = "enter an integer for the number of times you want to run"
items = [
    'Enter the websites as a list items'
]

#code for opening the pages randomly
for i in range(times):
    print("running for the {} time.".format(i))
    list_int = random.randint(0,len(items))
    driver.get(videos[vid_int])
    int = random.randint(5,10)
    #if you the views dont count, try increasing the time range
    time.sleep(int)

#quiting the browser
driver.quit() 