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


## create new task.
click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
click_title.click()
click_title.send_keys('task_1')
save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()


# list all task under the query class
print("start")
driver.find_element_by_id('com.ticktick.task:id/toolbar').click()
driver.find_element_by_xpath("//android.widget.ImageButton[@index='0']").click()
print("start1")
driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[@index='3']").click()
print("done")

