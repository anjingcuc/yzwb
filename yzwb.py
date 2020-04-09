# -*- coding=utf8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time


def go_forward(d, url, css_selector):
    while True:
        d.get(url)

        try:
            element = WebDriverWait(d, 1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
            )

            if url == d.current_url:
                return element

        except TimeoutException:
            continue


driver = webdriver.Chrome()

username_input = go_forward(driver,
                            "https://account.chsi.com.cn/passport/login?entrytype=yzgr&service=http%3A%2F%2Fyz.chsi.com.cn%2Fj_spring_cas_security_check",
                            '#username')
username_input.send_keys('12312312')  # 替换成用户名

password_input = driver.find_element_by_css_selector('#password')
password_input.send_keys('123123123')  # 替换成密码

login_button = driver.find_element_by_css_selector('#fm1 > div.yz-pc-loginbtn > input.yz_btn_login')
login_button.click()

agree_btn = go_forward(driver, 'https://yz.chsi.com.cn/apply/newApply.do', '#agree-btn')
next_page = agree_btn.get_attribute('href')

agree_btn = go_forward(driver, next_page, '#agree-btn')
next_page = agree_btn.get_attribute('onclick')

city = go_forward(driver, 'https://yz.chsi.com.cn' + next_page[15:-1], '#zsdwss')
city_select = Select(city)
school_select = Select(driver.find_element_by_css_selector('#zsdwdm'))
method_select = Select(driver.find_element_by_css_selector('#ksfsm'))
plan_select = Select(driver.find_element_by_css_selector('#zxjh'))

while True:
    city_select.select_by_visible_text('北京市')  # 替换成自己想要考的大学所在城市
    if len(school_select.options) < 2:
        city_select.select_by_visible_text('省（市）')
    else:
        break

school_select.select_by_visible_text('北京XX大学')  # 替换成自己想要考的大学
method_select.select_by_visible_text('全国统考')  # 替换成自己的考试方式
plan_select.select_by_visible_text('无')  # 替换成自己的计划

next_btn = driver.find_element_by_css_selector('#next-step')
next_btn.click()

blank = driver.find_element_by_css_selector('#xmpy')
blank.send_keys('L')  # 替换成自己的姓名拼音

blank = Select(driver.find_element_by_css_selector('#xyjrm'))
blank.select_by_visible_text('非现役军人')  # 替换成自己的服役状态

blank = Select(driver.find_element_by_css_selector('#mzm'))
blank.select_by_visible_text('汉族')  # 替换成自己的民族

blank = driver.find_element_by_css_selector('label[for=xbm_1]')  # 替换成自己的性别     男生xbm_0  女生xbm_1
blank.click()

blank = driver.find_element_by_css_selector('label[for=hfm_0]')  # 替换成自己的婚姻状态     未婚hfm_0  已婚hfm_1 依次增加
blank.click()

blank = Select(driver.find_element_by_css_selector('#zzmmm'))
blank.select_by_visible_text('中国共产主义青年团团员')  # 替换成自己的政治面貌

blank = driver.find_element_by_css_selector('#txdz')
blank.send_keys('北京市朝阳区定福庄东街一号中国传媒大学')  # 替换成自己的通信地址

blank = driver.find_element_by_css_selector('#yzbm')
blank.send_keys('100024')  # 替换成自己的邮编

blank = driver.find_element_by_css_selector('#lxdh')
blank.send_keys('0')  # 替换成自己的固定电话

blank = driver.find_element_by_css_selector('#dzxx')
blank.send_keys('@qq.com')  # 替换成自己的邮箱

blank = Select(driver.find_element_by_css_selector('#kslym'))
blank.select_by_visible_text('普通全日制应届本科毕业生')  # 替换成自己的身份

blank = Select(driver.find_element_by_css_selector('#xxxs'))
blank.select_by_visible_text('普通全日制')  # 替换成自己的培养方式

blank = driver.find_element_by_css_selector('#zcxh')
blank.send_keys('2014')  # 替换成自己的学号

blank = Select(driver.find_element_by_css_selector('#bydwssm'))
blank1 = Select(driver.find_element_by_css_selector('#bydwm'))

while True:
    blank.select_by_visible_text('北京市')  # 替换成自己的学校所在城市
    if len(blank1.options) < 2:
        blank.select_by_visible_text('请选择')
    else:
        break
blank1.select_by_visible_text('(10XXX3)XXXX大学')  # 替换成自己的学校

blank = Select(driver.find_element_by_css_selector('#byzydm'))
blank1 = Select(driver.find_element_by_css_selector('#byzydm2'))

while True:
    blank.select_by_visible_text('0XXX2-XXXX学类')  # 替换成自己的专业类型
    if len(blank1.options) < 2:
        blank.select_by_visible_text('请选择')
    else:
        break
blank1.select_by_visible_text('0XXXX5-XXXX')  # 替换成自己的专业

blank = Select(driver.find_element_by_css_selector('#bklbm'))
blank.select_by_visible_text('非定向就业')  # 替换成自己的就业方式

blank = driver.find_element_by_css_selector('#sub-btn')
blank.click()

blank = Select(driver.find_element_by_css_selector('#jgss'))
blank1 = Select(driver.find_element_by_css_selector('#jgdjs'))
blank2 = Select(driver.find_element_by_css_selector('#jgszdm'))

while True:
    blank.select_by_visible_text('省')  # 替换成自己的籍贯省份
    if len(blank1.options) < 2:
        blank.select_by_visible_text('请选择')
    else:
        break
while True:
    blank1.select_by_visible_text('市')  # 替换成自己的籍贯城市
    if len(blank1.options) < 2:
        blank1.select_by_visible_text('请选择')
    else:
        break
blank2.select_by_visible_text('区')  # 替换成自己的籍贯区

blank = Select(driver.find_element_by_css_selector('#hkszdss'))
blank1 = Select(driver.find_element_by_css_selector('#hkszddjs'))
blank2 = Select(driver.find_element_by_css_selector('#hkszdm'))

while True:
    blank.select_by_visible_text('省')  # 替换成自己的户口省份
    if len(blank1.options) < 2:
        blank.select_by_visible_text('请选择')
    else:
        break
while True:
    blank1.select_by_visible_text('市')  # 替换成自己的户口城市
    if len(blank1.options) < 2:
        blank1.select_by_visible_text('请选择')
    else:
        break
blank2.select_by_visible_text('区')  # 替换成自己的户口区

blank = driver.find_element_by_css_selector('#hkszdxxdz')
blank.send_keys('XX')  # 替换成自己的户口详细地址

blank = Select(driver.find_element_by_css_selector('#csdss'))
blank1 = Select(driver.find_element_by_css_selector('#csddjs'))
blank2 = Select(driver.find_element_by_css_selector('#csdm'))

while True:
    blank.select_by_visible_text('省')  # 替换成自己的出生省份
    if len(blank1.options) < 2:
        blank.select_by_visible_text('请选择')
    else:
        break
while True:
    blank1.select_by_visible_text('市')  # 替换成自己的出生城市
    if len(blank1.options) < 2:
        blank1.select_by_visible_text('请选择')
    else:
        break
blank2.select_by_visible_text('区')  # 替换成自己的出生区

blank = driver.find_element_by_css_selector('#xxgzdw')
blank.send_keys('XXXXXXXXX')  # 替换成自己的单位

blank = Select(driver.find_element_by_css_selector('#daszdss'))
blank1 = Select(driver.find_element_by_css_selector('#daszddjs'))
blank2 = Select(driver.find_element_by_css_selector('#daszdm'))

while True:
    blank.select_by_visible_text('北京市')  # 替换成自己的档案所在省份
    if len(blank1.options) < 2:
        blank.select_by_visible_text('请选择')
    else:
        break
while True:
    blank1.select_by_visible_text('市辖区')  # 替换成自己的档案所在城市
    if len(blank1.options) < 2:
        blank1.select_by_visible_text('请选择')
    else:
        break
blank2.select_by_visible_text('朝阳区')  # 替换成自己的档案所在区

blank = driver.find_element_by_css_selector('#daszdw')
blank.send_keys('中国传媒大学')  # 替换成自己的档案所在单位

blank = driver.find_element_by_css_selector('#daszdwdz')
blank.send_keys('北京市朝阳区定福庄东街一号')  # 替换成自己的档案所在单位地址

blank = driver.find_element_by_css_selector('#daszdwyzbm')
blank.send_keys('100024')  # 替换成自己的档案所在单位地址邮编

blank = driver.find_element_by_css_selector('#jlcf')
blank.send_keys('无')  # 替换成自己的奖惩状态

blank = driver.find_element_by_css_selector('#kszbqk')
blank.send_keys('无')  # 替换成自己的作弊情况

# 替换成自己的家属情况   四个栏分别为 姓名    关系  单位职务    电话
# 可以有三个 剩下两个 也是四栏 xingming1 guanxi1  danweizhiwu1  dianhua1
# 可以有三个 剩下两个 也是四栏 xingming2 guanxi2  danweizhiwu2  dianhua2
blank = driver.find_element_by_css_selector('#xingming0')
blank.send_keys('无')
blank = driver.find_element_by_css_selector('#guanxi0')
blank.send_keys('无')
blank = driver.find_element_by_css_selector('#danweizhiwu0')
blank.send_keys('无')
blank = driver.find_element_by_css_selector('#dianhua0')
blank.send_keys('13800138000')

# 替换成自己的家属情况   四个栏分别为 年月    单位  单位职务
# 和上面一样 其他经历请变动后面的数字
blank = driver.find_element_by_css_selector('#nianyue0')
blank.send_keys('无')
blank = driver.find_element_by_css_selector('#danwei0')
blank.send_keys('无')
blank = driver.find_element_by_css_selector('#zhiwu0')
blank.send_keys('无')

blank = driver.find_element_by_css_selector('#sub-btn')
blank.click()

blank = Select(driver.find_element_by_css_selector('#yxsm'))
blank1 = Select(driver.find_element_by_css_selector('#zydm'))
blank2 = Select(driver.find_element_by_css_selector('#yjfxm'))
blank3 = Select(driver.find_element_by_css_selector('#bkxxfs'))
blank4 = Select(driver.find_element_by_css_selector('#kskm'))

while True:
    blank.select_by_visible_text('(012)中文学院')   # 报考的学院
    if len(blank1.options) < 2:
        blank.select_by_visible_text('请选择')
    else:
        break
while True:
    blank1.select_by_visible_text('(XXXX0)(XXXX育') # 报考的专业
    if len(blank1.options) < 2:
        blank1.select_by_visible_text('请选择')
    else:
        break
while True:
    blank2.select_by_visible_text('(CX)XXXX教育') # 报考的方向
    if len(blank1.options) < 2:
        blank2.select_by_visible_text('请选择')
    else:
        break
while True:
    blank3.select_by_visible_text('(1)全日制')  # 报考的学制
    if len(blank1.options) < 2:
        blank3.select_by_visible_text('请选择')
    else:
        break
blank4.select_by_visible_text('(101)思想政治理论|(201)英语一|(354)汉语基础|(445)汉语国际教育基础') # 考试科目

blank = driver.find_element_by_css_selector('#sub-btn')
blank.click()

blank = Select(driver.find_element_by_css_selector('#bmdss'))
blank1 = Select(driver.find_element_by_css_selector('#bmddm'))

while True:
    blank.select_by_visible_text('北京市') # 考试城市
    if len(blank1.options) < 2:
        blank.select_by_visible_text('请选择')
    else:
        break
blank1.select_by_visible_text('北京XXX大学') # 考点

blank = driver.find_element_by_css_selector('#sub-btn')
blank.click()
