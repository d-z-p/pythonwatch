import unittest

from main import *
import unittest
from selenium import webdriver

from appium.webdriver.common.touch_action import TouchAction
class MyTestCase(unittest.TestCase):

    def test_case01(self):







       # driver.find_element(By.ID, "com.jx.launcher:id/ivGif").click()
      # sleep(20)
         TouchAction(driver).tap(x=281, y=211).perform()
         TouchAction(driver).tap(x=283, y=223).perform()
         TouchAction(driver).tap(x=211, y=359).perform()
         TouchAction(driver).tap(x=58, y=31).perform()
         TouchAction(driver).tap(x=58, y=31).perform()
         TouchAction(driver).tap(x=73, y=360).perform()
         TouchAction(driver).tap(x=222, y=357).perform()
         TouchAction(driver).tap(x=259, y=257).perform()







       # driver.minimize_window() 最小化窗口





    # def test_case02(self):



    # def test_case3(self):#微聊

      


if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    #suite.addTest(MyTestCase("test_case00"))
    suite.addTest(MyTestCase("test_case01"))
    # suite.addTest(MyTestCase("test_case02"))
    # suite.addTest(MyTestCase("test_case03"))
    #suite.addTest(MyTestCase("test_case03"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)