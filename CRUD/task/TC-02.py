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


## create new task that input has phone number.
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('0987123456 task_12')

    ## pick priority toggle.
    driver.find_element_by_id('com.ticktick.task:id/priority_toggle').click()
    driver.find_element_by_xpath('//android.widget.RelativeLayout/android.widget.RadioButton').click()

    ## add tag.
    driver.find_element_by_id('com.ticktick.task:id/tag_toggle').click()
    # touch.
    action = TouchAction(driver)
    action.tap(x=645,y=1392).release().perform()
    time.sleep(1)
    action.tap(x=488,y=939).release().perform()
    time.sleep(1)
   
    ## choose inbox.
    driver.find_element_by_id('com.ticktick.task:id/project_layout').click()
    driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[@text='Inbox']").click()

    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
    driver.find_element_by_id('com.ticktick.task:id/list').click()
    driver.find_element_by_xpath("//android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.view.View[@index='0']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//android.widget.ImageButton").click()
except:
    print('error of create new task with phone number.')


## create new task in different inbox.
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('9:00 6/31 task_13')

    ## pick priority toggle.
    driver.find_element_by_id('com.ticktick.task:id/priority_toggle').click()
    driver.find_element_by_xpath('//android.widget.RelativeLayout/android.widget.RadioButton').click()

    ## add tag.
    driver.find_element_by_id('com.ticktick.task:id/tag_toggle').click()
    # touch.
    action = TouchAction(driver)
    action.tap(x=645,y=1392).release().perform()
    time.sleep(1)
    action.tap(x=488,y=939).release().perform()
    time.sleep(1)
   
    ## choose inbox.
    driver.find_element_by_id('com.ticktick.task:id/project_layout').click()
    driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[@text='Add Lists']").click()
    create_taskList = driver.find_element_by_id('com.ticktick.task:id/text_create_tasklist')
    create_taskList.send_keys('work')
    driver.find_element_by_id('android:id/button1').click()  # button ok.

    # save task and show .
    driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
    driver.find_element_by_xpath('//android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageButton').click()
    time.sleep(1)
    driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[@text='work']").click()

except:
    print('error of create new task in different inbox.')

