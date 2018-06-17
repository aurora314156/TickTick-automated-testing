from appium import webdriver

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
## create new task in calendar.
## create new task.
driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
click_title.click()
click_title.send_keys('task_1_calendar')
save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()

# TC-07
## edit task in calendar.
driver.find_element_by_id('com.ticktick.task:id/list').click()
driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.view.View[@index='2']").click()
edit_task_1 = driver.find_element_by_id('com.ticktick.task:id/edit_text')
edit_task_1.click()
edit_task_1.send_keys('task_1_edited')
driver.find_element_by_xpath("//android.widget.ImageButton").click()

# TC-08
## done task in calendar.
driver.find_element_by_id('com.ticktick.task:id/list').click()
driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.view.View[@index='2']").click()
Checkbox = driver.find_element_by_id('com.ticktick.task:id/task_checkbox').click()
driver.find_element_by_xpath("//android.widget.ImageButton").click()

# TC-o9
## delete task in calender.
driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.view.View[@index='2']").click()
tool_bar = driver.find_element_by_id('com.ticktick.task:id/toolbar').click()
driver.find_element_by_xpath("//android.support.v7.widget.LinearLayoutCompat/android.widget.ImageView[@index='0']").click()
driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[@index='9']").click()