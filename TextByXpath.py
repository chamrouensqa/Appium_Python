from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel-3'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
desired_caps['app'] = ('/Users/chamrouen/Downloads/Android_Demo_App.apk')

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

ele_xpath1 = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Btn1"]')
ele_xpath1.click()
time.sleep(2)

ele_xpath2 = driver.find_element(AppiumBy.XPATH,'//android.widget.EditText')
ele_xpath2.send_keys("Rouen Pro")
time.sleep(2)

ele_xpath3 = driver.find_element(AppiumBy.XPATH,'//android.widget.Button')
ele_xpath3.click()
time.sleep(2)

driver.quit()