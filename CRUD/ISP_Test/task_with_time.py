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

## normal time (00:00).
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('00:00')

    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with normal time(00:00).')

## normal time (01:00).
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('01:00')

    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with normal time(01:00).')

## normal time (12:00).
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('12:00')

    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with normal time(12:00).')

## normal time (24:00).
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('24:00')

    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with normal time(24:00).')


## illegal hour (25:00).
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('25:00')

    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with illegal time(25:00).')


## illegal hour (-1:00).
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('-1:00')

    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with illegal time(-1:00).')

## illegal hour (one:00).
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('one:00')

    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with illegal time(one:00).')

## illegal hour (Null:00).
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys(':00')

    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with illegal time(Null:00).')



### minute.


## illegal minute (00:01).
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('00:01')

    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with illegal time(00:01).')


## illegal minute (00:60).
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('00:60')

    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with illegal time(00:60).')

## illegal minute (00:-10).
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('00:-10')

    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with illegal time(00:-10).')

## illegal minute (00:61).
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('00:61')

    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with illegal time(00:61)')

## illegal minute (00:null).
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('00:')

    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with illegal time(00:Null)')

## illegal minute (00:S).
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('00:S')

    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with illegal time(00:S)')