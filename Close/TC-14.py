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
print(2)
driver.find_element_by_id('com.ticktick.task:id/photo').click()
driver.find_element_by_id('com.ticktick.task:id/sign_in_up_btn').click()
print(7)
account = driver.find_element_by_xpath("//android.widget.EditText[@index='0']")
time.sleep(1)
account.send_keys('wirlner2018@gmail.com')
time.sleep(1)
print(8)
password = driver.find_element_by_id("com.ticktick.task:id/account_login_in_edit_password")
time.sleep(1)
password.send_keys('wiki1424')

print(9)
driver.find_element_by_id('com.ticktick.task:id/login_in_btn').click()
print(10)
time.sleep(5)
print(11)
driver.find_element_by_id('com.ticktick.task:id/ok').click()
print(12)
time.sleep(5)
driver.find_element_by_id('com.ticktick.task:id/icon').click()
print(13)
#driver.find_element_by_xpath('//android.view.ViewGroup/android.widget.FrameLayout[@index='2']/android.widget.RelativeLayout[@index='1']').click()
driver.find_element_by_id('com.ticktick.task:id/navigation_settings_id').click()
print(1)
driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[@index='6']").click()
print(3)
driver.find_element_by_xpath("//android.widget.ListView/android.widget.RelativeLayout[@index='1']").click()
print(4)
driver.find_element_by_id('android:id/checkbox').click()
print(5)
#driver.find_element_by_id('android:id/button1').click()
#print(6)

