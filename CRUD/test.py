from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.ticktick.task'
desired_caps['appActivity'] = 'activity.DispatchActivity'
desired_caps['skipUnlock'] = 'true'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


# test Task General.
driver.find_element_by_id('com.ticktick.task:id/skip_tutorial').click()
## create new task.
click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title').click()
click_title.send_keys('hello')