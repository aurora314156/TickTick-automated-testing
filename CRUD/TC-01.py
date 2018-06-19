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

# TC-01
## create new task with string.
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('task_one(string)')

    ## pick up time and date.
    driver.find_element_by_id('com.ticktick.task:id/pick_up_time').click()
    driver.find_element_by_id('com.ticktick.task:id/item1').click()

    ## pick priority toggle.
    driver.find_element_by_id('com.ticktick.task:id/priority_toggle').click()
    driver.find_element_by_xpath('//android.widget.RelativeLayout/android.widget.RadioButton').click()

    # ## add tag.
    # driver.find_element_by_id('com.ticktick.task:id/tag_toggle').click()
    # add_tag = driver.find_element_by_id('com.ticktick.task:id/quick_add_title').send_keys('tag')
   
    ## choose inbox.
    driver.find_element_by_id('com.ticktick.task:id/project_layout').click()
    driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[@text='Inbox']").click()
    # create_taskList = driver.find_element_by_id('com.ticktick.task:id/text_create_tasklist')
    # create_taskList.send_keys('work')
    # driver.find_element_by_id('android:id/button1').click()  # button ok.

    # save task and show .
    save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
    # driver.find_element_by_xpath('//android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageButton').click()
    # driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[@text='work']").click()

except:
    print('error of create new task with string.')

# ## create new task with int 1.
# try:
#     click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
#     click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
#     click_title.click()
#     click_title.send_keys('1')
#     save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
# except:
#     print('error of create new task with int 1.')

# ## create new task with int -1.
# try:
#     click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
#     click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
#     click_title.click()
#     click_title.send_keys('-1')
#     save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
# except:
#     print('error of create new task with int -1.')

# ## create new task with int 0.
# try:
#     click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
#     click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
#     click_title.click()
#     click_title.send_keys('0')
#     save_btn = driver.find_element_by_id('com.ticktick.task:id/save_btn').click()
# except:
#     print('error of create new task with int 0.')

