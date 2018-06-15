from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.google.android.dialer'
desired_caps['appActivity'] = 'DialtactsActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


