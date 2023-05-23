# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "8.1.0"
caps["deviceName"] = "85110081464811"
caps["appPackage"] = "com.jx.launcher"
caps["appActivity"] = "com.zmapp.activity.PlaysimActivity"
caps["appWaitForLaunch"] = "false"
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

# 获取屏幕宽度
width = driver.get_window_size()['width']

# 获取屏幕高度
height = driver.get_window_size()['height']

driver.implicitly_wait(10)
ac = driver.current_activity
print(ac)



