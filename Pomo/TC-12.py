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



#driver.find_element_by_id('com.ticktick.task:id/page_navigation_layout').click()
#print(1)
driver.find_element_by_id('com.ticktick.task:id/navigation_settings_id').click()
print(2)
driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[@index='7']").click()
print(3)
driver.find_element_by_id('android:id/checkbox').click()
print(4)
driver.find_element_by_id('com.ticktick.task:id/toolbar').click()
print(5)
driver.find_element_by_xpath("//android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageButton").click()
print(6)
driver.find_element_by_id('com.ticktick.task:id/navigation_pomo_id').click()
print("start pomo timer")
