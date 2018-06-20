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

# TC-02
## create new task that input date before time.
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('6/31 9:00 task_1')

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
    time.sleep(1)

    ## choose inbox.
    driver.find_element_by_id('com.ticktick.task:id/project_layout').click()
    driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[@text='Inbox']").click()

    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('error of create new task with string.')


## create new task that input time before date.
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('9:00 6/31 task_2')

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
except:
    print('error of create new task with string.')


try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('-2:00 task_3')

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
except:
    print('error of create new task with wrong time(-2:00).')

try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('0:-20 task_4')

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
except:
    print('error of create new task with wrong time(0:-20).')

try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('-2:-20 task_5')

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
except:
    print('error of create new task with wrong time(-3:-20).')

try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('0:00 task_6')

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
except:
    print('error of create new task with wrong time(0:00).')



## create new task that input date is wrong.
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('13/2 task_7')

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
except:
    print('error of create new task with wrong date.')


try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('0/2 task_8')

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
except:
    print('error of create new task with wrong date(0/2).')


try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('6/0 task_9')

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
except:
    print('error of create new task with wrong date(6/0).')


try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('6/31 task_10')

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
except:
    print('error of create new task with wrong date(6/31).')

try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('-10/-10 task_11')

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
except:
    print('error of create new task with wrong date.(-10/-10)')


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
