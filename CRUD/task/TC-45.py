from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.ticktick.task'
desired_caps['appActivity'] = '.activity.MeTaskActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
## skip_tutorial.
try:
    driver.find_element_by_id('com.ticktick.task:id/skip_tutorial').click()
except:
    print('initial error.')

# create task.
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('task_1')

    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
except:
    print('create task error.')

# TC-04
try:
## done task.
    driver.find_element_by_xpath("//android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.view.View[@index='0']").click()
    Checkbox = driver.find_element_by_id('com.ticktick.task:id/task_checkbox').click()
    driver.find_element_by_xpath("//android.widget.ImageButton").click()
except:
    print('TC-04 error.')

# TC-05
try:
## delete task.
    driver.find_element_by_xpath("//android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.view.View[@index='0']").click()
    tool_bar = driver.find_element_by_id('com.ticktick.task:id/toolbar').click()
    driver.find_element_by_xpath("//android.support.v7.widget.LinearLayoutCompat/android.widget.ImageView[@index='0']").click()
    driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[@index='9']").click()
except:
    print('TC-05 error.')