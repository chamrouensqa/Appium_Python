import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel-3'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
desired_caps['app'] = ('/Users/chamrouen/Downloads/Android_Demo_App.apk')

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

ele_id = driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/EnterValue")
print("Text on the button",ele_id.text)
print("Text on the attribute",ele_id.get_attribute("text"))
print("Content desc on the attribute",ele_id.get_attribute("content-desc"))
ele_id.click()

time.sleep(2)
