#-*- coding: UTF-8 -*-
from selenium import webdriver#加载webdriver方法
import time#导入time包
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()#创建Chrome对象，使用Chrome浏览器
driver.get('http://baidu.com')#在Chrome输入访问网址
time.sleep(3)#设置等待时间
driver.maximize_window()#窗口最大化
# driver.set_window_size(800,600)#设置窗口大小
#这里为什么要\\呢，\t是个制表符，需要加多\做转义
# driver.get_screenshot_as_file('d\\test.png')
driver.refresh()#浏览器刷新页面
#Id元素定位

# driver.find_element_by_link_text("登录")
# driver.find_element_by_id("kw").send_keys("吴亦凡")
# driver.find_element_by_id("cnmoBbs_password").send_keys("python"))
#如果有多个相同的元素值时
# driver.find_elements_by_class_name("")[1].click()

#xpath定位
driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
#索引
time.sleep(10)
# driver.find_element_by_id("submit").click()
switch
driver.quit()



