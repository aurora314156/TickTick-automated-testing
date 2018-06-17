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



driver.find_element_by_id('com.ticktick.task:id/navigation_settings_id').click()
print(2)
driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[@index='7']").click()
print(3)
driver.find_element_by_id('android:id/checkbox').click()
print(4)
driver.find_element_by_xpath("//android.widget.ListView/android.widget.RelativeLayout[@index='9']").click()
print(6)
driver.find_element_by_xpath("//android.widget.ListView/android.widget.RelativeLayout[@index='10']").click()

def swipeUp(driver, t=500, n=1):
    l = driver.get_window_size()
    x1 = l['width'] * 0.5     # x坐标
    y1 = l['height'] * 0.75   # 起始y坐标
    y2 = l['height'] * 0.25   # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)
print("往上滑螢幕")
swipeUp(driver)
print(7)
driver.find_element_by_xpath("//android.widget.ListView/android.widget.RelativeLayout[@index='11']").click()
print(8)
driver.find_element_by_id('com.ticktick.task:id/toolbar').click()
print(9)
driver.find_element_by_xpath("//android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageButton").click()
print(10)
driver.find_element_by_id('com.ticktick.task:id/navigation_pomo_id').click()
print("start pomo timer")
driver.find_element_by_id('com.ticktick.task:id/right_btn').click()
print("done")