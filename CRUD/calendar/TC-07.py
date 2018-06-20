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
driver.find_element_by_id('com.ticktick.task:id/skip_tutorial').click()

## click calendar.
driver.find_element_by_id('com.ticktick.task:id/navigation_calendar_id').click()

try:
## create new task.
    driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('calendar1')

    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('create new task error.')

# TC-07_1 change the date that in future.
try:
## edit task in calendar.
    driver.find_element_by_id('com.ticktick.task:id/list').click()
    driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.view.View[@index='2']").click()
    ## edit date.
    driver.find_element_by_id('com.ticktick.task:id/task_date_text').click()
    time.sleep(1)
    # touch.
    action = TouchAction(driver)
    action.tap(x=993,y=797).release().perform()
    driver.find_element_by_xpath("//android.widget.ImageButton").click()

    ## edit task name.
    edit_task_1 = driver.find_element_by_id('com.ticktick.task:id/edit_text')
    edit_task_1.click()
    edit_task_1.send_keys('calendar1_date_future')

    ## edit priority.
    driver.find_element_by_id('com.ticktick.task:id/priority_toggle').click()
    driver.find_element_by_xpath("//android.widget.RelativeLayout[@index='1']/android.widget.RadioButton").click()

    ## add task_kind.
    description = driver.find_element_by_id('com.ticktick.task:id/task_editor_composite')
    description.click()
    description.send_keys('item1')
    driver.find_element_by_id('com.ticktick.task:id/input_task_kind').click()

    ## edit tag.
    driver.find_element_by_id('com.ticktick.task:id/input_tag').click()
    time.sleep(1)
    action = TouchAction(driver)
    action.tap(x=645,y=1543).release().perform()
    time.sleep(1)
    action.tap(x=594,y=1233).release().perform()
    time.sleep(1)
    action.tap(x=271,y=1239).release().perform()
    time.sleep(1)
    action.tap(x=987,y=1686).release().perform()
    time.sleep(1)
    driver.find_element_by_id('com.ticktick.task:id/flexbox_layout').click()
    driver.find_element_by_id('android:id/button1').click()

    ## show
    driver.find_element_by_xpath("//android.widget.ImageButton").click()
    time.sleep(1)
    action.tap(x=993,y=389).release().perform()
except:
    print('TC-07 change to future date error.')


# TC-07_2 change the date that in past.
try:
## edit task in calendar.
    driver.find_element_by_id('com.ticktick.task:id/list').click()
    driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.view.View[@index='2']").click()
    ## edit date.
    driver.find_element_by_id('com.ticktick.task:id/task_date_text').click()
    time.sleep(1)
    # touch.
    action = TouchAction(driver)
    action.tap(x=79,y=797).release().perform()
    driver.find_element_by_xpath("//android.widget.ImageButton").click()

    driver.find_element_by_xpath("//android.widget.ImageButton").click()
    time.sleep(1)
    action.tap(x=70,y=389).release().perform()
except:
    print('TC-07 to past date error.')