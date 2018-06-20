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

# create new task.
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('task_1')

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

    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('create task error.')

# TC-03
try:
    ## edit task_name.
    driver.find_element_by_id('com.ticktick.task:id/list').click()
    driver.find_element_by_xpath("//android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.view.View[@index='0']").click()
    edit_task_1 = driver.find_element_by_id('com.ticktick.task:id/edit_text')
    edit_task_1.click()
    edit_task_1.send_keys('task_1_edited')

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
    driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[@index='1']").find_element_by_id('com.ticktick.task:id/checkbox').click()
    driver.find_element_by_id('android:id/button1').click()

    ## show
    driver.find_element_by_xpath("//android.widget.ImageButton").click()
except:
    print('TC-03 error.')