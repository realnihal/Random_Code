from selenium import webdriver
import time
import random

driver = webdriver.Chrome('/usr/local/bin/chromedriver')

videos = [
    'https://underthesun19.blogspot.com/',
    'https://underthesun19.blogspot.com/2020/04/bharathiyar-says.html',
    'https://underthesun19.blogspot.com/2020/05/feminism.html',
    'https://underthesun19.blogspot.com/2020/07/fear.html',
    'https://underthesun19.blogspot.com/2020/08/what-is-activism-at-its-finest.html',
    'https://underthesun19.blogspot.com/2020/08/silence.html#more',
    'https://underthesun19.blogspot.com/2020/08/an-odyssey-tryst-with-myself.html#more',
    'https://underthesun19.blogspot.com/2020/08/part-1-homesickness.html#more'
    ]

for i in range(1000):
    print("running for the {} time.".format(i))
    vid_int = random.randint(0,7)
    driver.get(videos[vid_int])
    int = random.randint(5,10)
    time.sleep(int)

driver.quit() 
