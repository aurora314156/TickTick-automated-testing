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
try:
    driver.find_element_by_id('com.ticktick.task:id/skip_tutorial').click()
except:
    print('initial error.')

# tag
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('normal_tag')

    ## add tag.
    driver.find_element_by_id('com.ticktick.task:id/tag_toggle').click()
    # touch.
    action = TouchAction(driver)
    action.tap(x=645,y=1392).release().perform()
    time.sleep(1)
    action.tap(x=808,y=1236).release().perform()

    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
    driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.view.View[@index='0']").click()
    driver.find_element_by_xpath("//android.widget.ImageButton").click()
except:
    print('error of create new task with string.')

# null tag.
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('null_tag')

    ## add tag.
    driver.find_element_by_id('com.ticktick.task:id/tag_toggle').click()
    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
    driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.view.View[@index='0']").click()
    driver.find_element_by_xpath("//android.widget.ImageButton").click()
except:
    print('error of create null tag.')

# positive tag.
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('positive_tag')

    ## add tag.
    driver.find_element_by_id('com.ticktick.task:id/tag_toggle').click()
    # touch.
    action = TouchAction(driver)
    action.tap(x=91,y=1687).release().perform()
    time.sleep(1)
    action.tap(x=810,y=1240).release().perform()
    time.sleep(1)
    action.tap(x=697,y=1236).release().perform()

    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
    driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.view.View[@index='0']").click()
    driver.find_element_by_xpath("//android.widget.ImageButton").click()
except:
    print('error of create positive tag.')

# negative tag.
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('negative_tag')

    ## add tag.
    driver.find_element_by_id('com.ticktick.task:id/tag_toggle').click()
    # touch.
    action = TouchAction(driver)
    action.tap(x=91,y=1687).release().perform()
    time.sleep(1)
    action.tap(x=588,y=1391).release().perform()
    time.sleep(1)
    action.tap(x=810,y=1240).release().perform()
    time.sleep(1)
    action.tap(x=697,y=1236).release().perform()

    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
    driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.view.View[@index='0']").click()
    driver.find_element_by_xpath("//android.widget.ImageButton").click()
except:
    print('error of create negative tag.')

# symbol tag.
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('symbol_tag')

    ## add tag.
    driver.find_element_by_id('com.ticktick.task:id/tag_toggle').click()
    # touch.
    action = TouchAction(driver)
    action.tap(x=91,y=1687).release().perform()
    time.sleep(1)
    action.tap(x=169,y=1395).release().perform()
    time.sleep(1)

    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
    driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.view.View[@index='0']").click()
    driver.find_element_by_xpath("//android.widget.ImageButton").click()
except:
    print('error of create symbol tag.')

# # limit tag.
# try:
#     click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
#     click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
#     click_title.click()
#     click_title.send_keys('limit_tag')

#     ## add tag.
#     driver.find_element_by_id('com.ticktick.task:id/tag_toggle').click()
#     add_tag.click()
#     add_tag.send_keys('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

#     # save task and show .
#     save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
# except:
#     print('error of create limit tag.')