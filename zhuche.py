# http://118.31.19.120:3000/
# zhuche 邮件不会发
# 远程链接到数据库改数据
# 周三前完成
# 作业要求：1、测试用例，用代码注释的方法；2、至少用三个测试用例 3、加分：把测试用例放到csv或者excel 文件里读取

# 疑问，1、注册页面为什么定位元素用xpath失败？  2、怎样自动打印出页面的提示语？


'''
Created on 2018-01-16
@author: sunyu
Project:论坛登录测试用例
'''
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="./chromedriver")
# 打开注册页面
url = "http://118.31.19.120:3000/"
driver.get(url)
# 点击注册按钮
loginXpath = "/html/body/div[1]/div/div/ul/li[5]/a"
driver.find_element_by_xpath(loginXpath).click()
#  输入合法的注册信息
loginNameId = "loginname"
passwdId = 'pass'
qrpasswdId = 're_pass'
emailId = 'email'
driver.find_element_by_id(loginNameId).send_keys("bb123")
driver.find_element_by_id(passwdId).send_keys("bb123")
driver.find_element_by_id(qrpasswdId).send_keys("bb123")
driver.find_element_by_id(emailId).send_keys("136162509@qq.com")
# 点击注册按钮
loginBtnClassName = 'span-primary'
driver.find_element_by_class_name(loginBtnClassName).click()

# 输入不合法的用户信息－用户名不合法
try:
    #  清除之前输入的文本信息
    driver.find_element_by_id(loginNameId).clear()
    driver.find_element_by_id(emailId).clear()
    print ('test pass: clean successful')
    driver.find_element_by_id(loginNameId).send_keys("da[];<>")
    driver.find_element_by_id(passwdId).send_keys("bb123")
    driver.find_element_by_id(qrpasswdId).send_keys("bb123")
    driver.find_element_by_id(emailId).send_keys("136162509@qq.com")
    loginBtnClassName = 'span-primary'
    driver.find_element_by_class_name(loginBtnClassName).click()
    print ("用户名不合法")
except Exception as e:
    print ("Exception found",format(e))

# 输入不合法的用户信息－密码为空
try:
    driver.find_element_by_id(loginNameId).clear()
    driver.find_element_by_id(emailId).clear()
    print ('test pass: clean successful')
    driver.find_element_by_id(loginNameId).send_keys("cc123")
    driver.find_element_by_id(passwdId).send_keys("")
    driver.find_element_by_id(qrpasswdId).send_keys("")
    driver.find_element_by_id(emailId).send_keys("136162509@qq.com")
    loginBtnClassName = 'span-primary'
    driver.find_element_by_class_name(loginBtnClassName).click()
    print ("信息不完整")
except Exception as e:
    print ("Exception found",format(e))


