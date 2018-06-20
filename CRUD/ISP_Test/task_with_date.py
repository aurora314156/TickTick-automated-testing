from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.ticktick.task'
desired_caps['appActivity'] = '.activity.MeTaskActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
## skip_tutorial.
try:
    driver.find_element_by_id('com.ticktick.task:id/skip_tutorial').click()
except:
    print('initial error.')


## normal (1/10)
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('1/10')
    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with normal date.')

## normal (12/10)
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('12/10')
    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with normal date.')

##  month is zero (0/10)
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('0/10')
    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with date that month is zero.')

##  month exceed 12 (13/10)
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('13/10')
    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with date that month exceed 12.')

##  month is negative (-1/10)
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('-1/10')
    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with date that month is negative.')


##  month is string (S/10)
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('S/10')
    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with date that month is string.')

##  month is string (null/10)
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('/10')
    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with date that month is null.')

## day

## normal (1/1)
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('1/1')
    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with normal date.')

## normal (12/31)
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('12/31')
    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with normal date.')

##  day is zero (10/0)
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('10/0')
    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with date that day is zero.')

##  day exceed 31 (10/32)
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('10/32')
    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with date that day exceed 31.')

##  day is negative (10/-10)
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('10/-10')
    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with date that day is negative.')


##  day is string (10/S)
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('10/S')
    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with date that day is string.')

##  day is string (10/null)
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('10/')
    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with date that day is null.')

##  illegal date (6/31)
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('6/31')
    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with date that day is illegal.')

