from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.google.android.dialer'
desired_caps['appActivity'] = 'DialtactsActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



driver.find_element_by_id('com.google.android.dialer:id/search_box_start_search').click()
search_box = driver.find_element_by_id('com.google.android.dialer:id/search_view')
search_box.click()
search_box.send_keys('hello toby')