from webdriver_helper.pom import *

class BrucePage(BasePage):
    url='https://www.vipc6.com/'
    BT_login=LazyElement(
        By.XPATH,'/html/body/section/div[2]/div[1]/ul[2]/li/p/a[1]'
    )   
    IN_username=LazyElement(
        By.XPATH,'//*[@id="inputEmail"]'
    )
    IN_password=LazyElement(
        By.XPATH,'//*[@id="inputPassword"]'
    )
    BT_login2=LazyElement(
        By.XPATH,'//*[@id="sign-in"]/div[1]/input[1]'
    )
    def login(self,username,password):
        self.click(self.BT_login)
        self.send_keys(self.IN_username,username)
        self.send_keys(self.IN_password,password)
        self.click(self.BT_login2)