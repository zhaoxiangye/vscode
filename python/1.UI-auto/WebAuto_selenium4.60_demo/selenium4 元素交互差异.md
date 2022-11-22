## **元素交互**

**1、find_element_by_\*语法弃用**

~~# driver.find_element_by_id('kw').send_keys('软件测试')~~

正确用法如下：

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# driver.find_element_by_id('kw').send_keys('软件测试')
driver.find_element(By.ID, 'kw').send_keys('软件测试')
input("......")
driver.quit()
```