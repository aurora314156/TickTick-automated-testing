from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

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
    click_title.send_keys('task_1_calendar')

    ## pick up time and date.
    driver.find_element_by_id('com.ticktick.task:id/pick_up_time').click()
    driver.find_element_by_id('com.ticktick.task:id/item1').click()

    ## pick priority toggle.
    driver.find_element_by_id('com.ticktick.task:id/priority_toggle').click()
    driver.find_element_by_xpath('//android.widget.RelativeLayout/android.widget.RadioButton').click()

    ## choose inbox.
    driver.find_element_by_id('com.ticktick.task:id/project_layout').click()
    driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[@text='Inbox']").click()

    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('TC-06 error.')

# TC-07
try:
## edit task in calendar.
    driver.find_element_by_id('com.ticktick.task:id/list').click()
    driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.view.View[@index='2']").click()
    ## edit date.
    driver.find_element_by_id('com.ticktick.task:id/task_date_text').click()
    # touch.
    # view_pager = driver.find_element_by_id('com.ticktick.task:id/viewpager')
    loc = driver.find_element_by_android_uiautomator('com.ticktick.task:id/viewpager').location
    size = driver.find_element_by_android_uiautomator('com.ticktick.task:id/viewpager').size
    print(loc,size)
    TouchAction(driver).tap(view_pager,None,1119).release()
    driver.find_element_by_xpath("//android.widget.ImageButton").click()

    ## edit task name.
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

    driver.find_element_by_xpath("//android.widget.ImageButton").click()
except:
    print('TC-07 error.')

# TC-08
try:
## done task in calendar.
    driver.find_element_by_id('com.ticktick.task:id/list').click()
    driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.view.View[@index='2']").click()
    Checkbox = driver.find_element_by_id('com.ticktick.task:id/task_checkbox').click()
    driver.find_element_by_xpath("//android.widget.ImageButton").click()
except:
    print('TC-08 error.')

# TC-09
try:
## delete task in calender.
    driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.view.View[@index='2']").click()
    tool_bar = driver.find_element_by_id('com.ticktick.task:id/toolbar').click()
    driver.find_element_by_xpath("//android.support.v7.widget.LinearLayoutCompat/android.widget.ImageView[@index='0']").click()
    driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[@index='9']").click()
except:
    print('TC-09 error.')