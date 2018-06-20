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

# TC-06
try:
## create new task in calendar.
## create new task.
    driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('calendar1')

    ## pick up time and date.
    driver.find_element_by_id('com.ticktick.task:id/pick_up_time').click()
    driver.find_element_by_id('com.ticktick.task:id/item1').click()

    ## pick priority toggle.
    driver.find_element_by_id('com.ticktick.task:id/priority_toggle').click()
    driver.find_element_by_xpath('//android.widget.RelativeLayout/android.widget.RadioButton').click()

    ## add tag.
    driver.find_element_by_id('com.ticktick.task:id/tag_toggle').click()
    # touch.
    action = TouchAction(driver)
    action.tap(x=645,y=1392).release().perform()
    time.sleep(1)
    action.tap(x=808,y=1236).release().perform()

    ## choose inbox.
    driver.find_element_by_id('com.ticktick.task:id/project_layout').click()
    driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[@text='Inbox']").click()

    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('TC-06 error of create new task in calendar with string.')


try:
## create new task in calendar with number.
    driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('1234567')

    ## pick up time and date.
    driver.find_element_by_id('com.ticktick.task:id/pick_up_time').click()
    driver.find_element_by_id('com.ticktick.task:id/item1').click()

    ## pick priority toggle.
    driver.find_element_by_id('com.ticktick.task:id/priority_toggle').click()
    driver.find_element_by_xpath('//android.widget.RelativeLayout/android.widget.RadioButton').click()
    
    ## add tag.
    driver.find_element_by_id('com.ticktick.task:id/tag_toggle').click()
    action = TouchAction(driver)
    action.tap(x=645,y=1392).release().perform()
    time.sleep(1)
    action.tap(x=488,y=939).release().perform()
    time.sleep(1)

    ## choose inbox.
    driver.find_element_by_id('com.ticktick.task:id/project_layout').click()
    driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[@text='Inbox']").click()

    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('TC-06 error of create new task in calendar with number.')

try:
## create new task in calendar with phone number.
    driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('0987123456')

    ## pick up time and date.
    driver.find_element_by_id('com.ticktick.task:id/pick_up_time').click()
    driver.find_element_by_id('com.ticktick.task:id/item1').click()

    ## pick priority toggle.
    driver.find_element_by_id('com.ticktick.task:id/priority_toggle').click()
    driver.find_element_by_xpath('//android.widget.RelativeLayout/android.widget.RadioButton').click()
    
    ## add tag.
    driver.find_element_by_id('com.ticktick.task:id/tag_toggle').click()
    action = TouchAction(driver)
    action.tap(x=645,y=1392).release().perform()
    time.sleep(1)
    action.tap(x=488,y=939).release().perform()
    time.sleep(1)

    ## choose inbox.
    driver.find_element_by_id('com.ticktick.task:id/project_layout').click()
    driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[@text='Inbox']").click()
    
    ## save and show.
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
    driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.view.View[@index='2']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//android.widget.ImageButton").click()

except:
    print('TC-06 error of create new task in calendar with number.')