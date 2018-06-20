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

## create new inbox.
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('string_inbox')

    ## choose inbox.
    driver.find_element_by_id('com.ticktick.task:id/project_layout').click()
    driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[@text='Add Lists']").click()
    create_taskList = driver.find_element_by_id('com.ticktick.task:id/text_create_tasklist')
    create_taskList.send_keys('string')
    driver.find_element_by_id('android:id/button1').click()  # button ok.

    # save task and show .
    driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
    driver.find_element_by_xpath('//android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageButton').click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[@text='string']").click()
except:
    print('error of create inbox.')


## create new null_inbox.
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('null_inbox')

    ## choose inbox.
    driver.find_element_by_id('com.ticktick.task:id/project_layout').click()
    driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[@text='Add Lists']").click()
    create_taskList = driver.find_element_by_id('com.ticktick.task:id/text_create_tasklist')
    create_taskList.send_keys('')
    driver.find_element_by_id('android:id/button1').click()  # button ok.
    time.sleep(3)
    driver.find_element_by_id('android:id/button2').click()  # button ok.
    driver.find_element_by_id('android:id/button2').click()  # button ok.
    # save task and show .
    driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create null_inbox.')

## create new positive_inbox.
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('positive_inbox')

    ## choose inbox.
    driver.find_element_by_id('com.ticktick.task:id/project_layout').click()
    driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[@text='Add Lists']").click()
    create_taskList = driver.find_element_by_id('com.ticktick.task:id/text_create_tasklist')
    create_taskList.send_keys('88')
    driver.find_element_by_id('android:id/button1').click()  # button ok.

    # save task and show .
    driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
    driver.find_element_by_xpath('//android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageButton').click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[@text='88']").click()
except:
    print('error of create positive_inbox.')


## create new negative_inbox.
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('negative_inbox')

    ## choose inbox.
    driver.find_element_by_id('com.ticktick.task:id/project_layout').click()
    driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[@text='Add Lists']").click()
    create_taskList = driver.find_element_by_id('com.ticktick.task:id/text_create_tasklist')
    create_taskList.send_keys('-88')
    driver.find_element_by_id('android:id/button1').click()  # button ok.

    # save task and show .
    driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
    driver.find_element_by_xpath('//android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageButton').click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[@text='-88']").click()
except:
    print('error of create negative_inbox.')

## create new symbol_inbox.
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('symbol_inbox')

    ## choose inbox.
    driver.find_element_by_id('com.ticktick.task:id/project_layout').click()
    driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[@text='Add Lists']").click()
    create_taskList = driver.find_element_by_id('com.ticktick.task:id/text_create_tasklist')
    create_taskList.send_keys('#')
    driver.find_element_by_id('android:id/button1').click()  # button ok.
    time.sleep(3)
    driver.find_element_by_id('android:id/button2').click()  # button ok.
    driver.find_element_by_id('android:id/button2').click()  # button ok.
    # save task and show .
    driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create symbol_inbox(#).')

## create new symbol_inbox(#).
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('symbol_inbox')

    ## choose inbox.
    driver.find_element_by_id('com.ticktick.task:id/project_layout').click()
    driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[@text='Add Lists']").click()
    create_taskList = driver.find_element_by_id('com.ticktick.task:id/text_create_tasklist')
    create_taskList.send_keys('@')
    driver.find_element_by_id('android:id/button1').click()  # button ok.

    # save task and show .
    driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
    driver.find_element_by_xpath('//android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageButton').click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[@text='@']").click()
except:
    print('error of create symbol_inbox(@).')



## test limit of inbox name.
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('symbol_inbox')

    ## choose inbox.
    driver.find_element_by_id('com.ticktick.task:id/project_layout').click()
    driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[@text='Add Lists']").click()
    create_taskList = driver.find_element_by_id('com.ticktick.task:id/text_create_tasklist')
    create_taskList.send_keys('@123@#######@@@@##############@@@@######@@@')
    driver.find_element_by_id('android:id/button1').click()  # button ok.

    # save task and show .
    driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
    driver.find_element_by_xpath('//android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageButton').click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[@text='@123@#######@@@@##############@@@@######@@@']").click()
except:
    print('error of create symbol_inbox.')