from webdriver_helper import get_webdriver
from pom import BrucePage

driver=get_webdriver()
driver.get(BrucePage.url)
page= BrucePage(driver)#实例化po
page.login('1139236503@qq.com','123qwe')
