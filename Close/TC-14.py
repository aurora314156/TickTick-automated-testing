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



driver.find_element_by_id('com.ticktick.task:id/navigation_settings_id').click()
time.sleep(1)
print(2)
driver.find_element_by_id('com.ticktick.task:id/photo').click()
time.sleep(1)
driver.find_element_by_id('com.ticktick.task:id/sign_in_up_btn').click()
time.sleep(1)
print(7)
account = driver.find_element_by_xpath("//android.widget.EditText[@index='0']")
time.sleep(2)
account.send_keys('wirlner2018@gmail.com')
time.sleep(2)
print(8)
password = driver.find_element_by_id("com.ticktick.task:id/account_login_in_edit_password")
time.sleep(2)
password.send_keys('wiki1424')
time.sleep(2)
print(9)
driver.find_element_by_id('com.ticktick.task:id/login_in_btn').click()
print(10)
time.sleep(5)
print(11)
driver.find_element_by_id('com.ticktick.task:id/ok').click()
print(12)
time.sleep(4)
driver.find_element_by_id('com.ticktick.task:id/icon').click()
time.sleep(1)
print(13)
driver.find_element_by_id('com.ticktick.task:id/navigation_settings_id').click()
time.sleep(1)
print(1)
driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[@index='6']").click()
time.sleep(1)
print(3)
driver.find_element_by_xpath("//android.widget.ListView/android.widget.RelativeLayout[@index='1']").click()
time.sleep(1)
print(4)
driver.find_element_by_id('android:id/checkbox').click()
time.sleep(1)
print(5)

# 模擬手指滑動
action = TouchAction(driver)
print(21)
action.long_press(x=245,y=869).move_to(x=833,y=855).move_to(x=822,y=1131).release().perform()
print(14)
time.sleep(4)
action = TouchAction(driver)
print(21)
action.long_press(x=245,y=869).move_to(x=833,y=855).move_to(x=822,y=1131).release().perform()
print(14)
time.sleep(4)
# 關閉安全鎖
driver.find_element_by_id('android:id/checkbox').click()
print(30)
time.sleep(2)
action.long_press(x=245,y=869).move_to(x=833,y=855).move_to(x=822,y=1131).release().perform()
print(31)

