import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# -*- coding: utf-8 -*-
# @CreateTime    : 2023.9.6
# @UpdateTime    : 2023.9.6
# @Author  : Always1172
# @File    : Course.py
# @说明：适用于北京邮电大学教务系统，可以实现抢课功能，仅为初始版本，未经过大规模测试，仅供本人练手使用，技术佬轻喷，请确保自己在校园网或vpn环境下使用
class Course(object):

    def start(self):
        ''' 1、登录教务系统 '''
        #此处输入自己的学号
        student_ID = "2020210794"
        #此处输入自己的教务系统密码
        passWord = "Lch010919"
        #此处输入自己要抢的课程的名称（尽量输入全称，否则有可能无法正确定位课程；若无法输入全称，请保证输入的名称可以少字但无错字）
        courseName = "社会创新与社会创业（双创）"
        #此处输入课程的授课教师名（有些课程会有不同教师授课，因此为了准确性，可以在此处输入教师名称，若不清楚教师名称，请保证字符串为“”）
        teacherName = "刘"
        #使用Chrome浏览器
        driver = webdriver.Chrome()
        driver.get("https://jwgl.bupt.edu.cn/jsxsd/")
        userAccount = driver.find_element(By.ID, "userAccount")
        userAccount.send_keys(student_ID)
        password = driver.find_element(By.ID, "userPassword")
        password.send_keys(passWord)
        driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        '''2、打开选课界面'''
        driver.find_element(By.XPATH, '//*[@class="cygn-content-move xsPerson"]/li').click()
        iframe = driver.find_element(By.ID, 'mainIframe')
        driver.switch_to.frame(iframe)
        driver.find_element(By.ID, "jrxk").click()
        driver.find_element(By.XPATH, '//*[@value=" 进入选课 "]').click()
        '''3、选课'''
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        #driver.find_element(By.XPATH, '//*[@id="topmenu"]/li[3]').click()
        #driver.switch_to.frame("mainFrame")
        # driver.find_element(By.ID, "dataView")
        # driver.find_elements(By.CLASS_NAME, 'center')
        while 1:
            driver.refresh()
            # 使用说明：必修选课请将数组标号改为2，选修选课请改为3，公选课请改为4，留级选课请改为5
            driver.find_element(By.XPATH, '//*[@id="topmenu"]/li[4]').click()
            driver.switch_to.frame("mainFrame")
            #课程名称
            driver.find_element(By.ID, "kcxx").send_keys(courseName)
            #授课教师名称
            driver.find_element(By.ID, "skls").send_keys(teacherName)
            driver.find_element(By.XPATH, '//*[@onclick="queryKxkcList()"]').click()
            driver.implicitly_wait(1)
            list_btn = driver.find_elements(By.LINK_TEXT, "选课")
            element = list_btn[0]
            element.click()
            confirm = driver.switch_to.alert
            confirm.accept()
            alert = driver.switch_to.alert
            alert.accept()
            driver.refresh();
            time.sleep(1)



if __name__ == '__main__':
    course = Course()
    course.start()

