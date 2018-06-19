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

# TC-03
try:
    click_button = driver.find_element_by_id('com.ticktick.task:id/add_task_btn').click()
    click_title = driver.find_element_by_id('com.ticktick.task:id/quick_add_title')
    click_title.click()
    click_title.send_keys('task_1')

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
    # driver.find_element_by_xpath('//android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageButton').click()
    # driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[@text='work']").click()


    ## edit task_name.
    driver.find_element_by_id('com.ticktick.task:id/list').click()
    driver.find_element_by_xpath("//android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.view.View[@index='0']").click()
    edit_task_1 = driver.find_element_by_id('com.ticktick.task:id/edit_text')
    edit_task_1.click()
    edit_task_1.send_keys('task_1_edited')

    ## edit priority.
    driver.find_element_by_id('com.ticktick.task:id/priority_toggle').click()
    driver.find_element_by_xpath("//android.widget.RelativeLayout[@index='1']/android.widget.RadioButton").click()

    ## add task_kind.
    description = driver.find_element_by_id('com.ticktick.task:id/task_editor_composite')
    description.click()
    description.send_keys('item1')
    driver.find_element_by_id('com.ticktick.task:id/input_task_kind').click()


    # ## edit tag.
    # edit_tag = driver.find_element_by_id('com.ticktick.task:id/input_tag')
    # edit_tag.click()
    # edit_tag.send_keys('tag1')


    driver.find_element_by_id('com.ticktick.task:id/input_close_keyboard').click()
    driver.find_element_by_xpath("//android.widget.ImageButton").click()
except:
    print('TC-03 error.')

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