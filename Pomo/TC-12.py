from appium import webdriver
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



#driver.find_element_by_id('com.ticktick.task:id/page_navigation_layout').click()
#print(1)
driver.find_element_by_id('com.ticktick.task:id/navigation_settings_id').click()
time.sleep(1)
print(2)
driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[@index='7']").click()
time.sleep(1)
print(3)
driver.find_element_by_id('android:id/checkbox').click()
time.sleep(1)
print(4)
driver.find_element_by_id('com.ticktick.task:id/toolbar').click()
time.sleep(1)
print(5)
driver.find_element_by_xpath("//android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageButton").click()
time.sleep(1)
print(6)
driver.find_element_by_id('com.ticktick.task:id/navigation_pomo_id').click()
time.sleep(1)
print("start pomo timer")
driver.find_element_by_id('com.ticktick.task:id/right_btn').click()
time.sleep(1)
print("done")