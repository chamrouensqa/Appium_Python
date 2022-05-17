import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.appium_service import AppiumService

appium_service = AppiumService()

# appium_service.start()

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel-3'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
desired_caps['app'] = ('/Users/chamrouen/Downloads/Android_Demo_App.apk')
desired_caps['noReset'] = True
# desired_caps['fullReset'] = True
# we cann used full reset to uninstall the application

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

ele_id = driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/EnterValue")
ele_id.click()

time.sleep(5)
driver.quit()
appium_service.stop()