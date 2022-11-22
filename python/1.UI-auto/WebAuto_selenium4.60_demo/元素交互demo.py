from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
'''
运行环境测试demo
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# driver.find_element_by_id('kw').send_keys('软件测试')
time.sleep(3)
driver.find_element(By.ID, 'kw').send_keys('软件测试')
time.sleep(3)
el1=driver.find_element(By.ID,'su')
el1.click()
time.sleep(5)
driver.quit()
'''
#------------------------------------------------------------------------------------
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
ele=driver.find_element(By.XPATH,'//*[@id="kw"]')
print(ele)#打印元素
print('元素的标签',ele.tag_name)
print('元素的大小位置',ele.rect)
ele.send_keys("丁")#对元素进行输入
print('输入框的内容',ele.get_attribute('value'))
ele.screenshot('ele.png')#为元素截图
btn=driver.find_element(By.XPATH,'//*[@id="su"]')
btn.click()
time.sleep(3)
driver.get_screenshot_as_file("click.png")#浏览器截图
#显示等待 允许自定义等待时机
ele2=WebDriverWait(driver,10).until(
    lambda _ :driver.find_element(
        By.XPATH,'//*[@id="su"]'
    )
)


#----------------------------------------------------------------------------
'''
POM
类表示页面
类属性 表示页面中的元素
类方法 表示对页面操作
'''
