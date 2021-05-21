# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

from selenium import webdriver

# browser = webdriver.Firefox()
# type(browser)
#
# browser.get('https://www.baidu.com')
#
# linkElem = browser.find_element_by_link_text('登录')
# linkElem.click()

#填写并提交表单
# browser = webdriver.Firefox()
# browser.get('https://mail.126.com')
# emailElem = browser.find_element_by_id('auto-id-1543204520931')
# emailElem.send_keys('qiaoddvip@126.com')
# passwordElem = browser.find_element_by_id('auto-id-1543204520934')
# passwordElem.send_keys('12345')
# passwordElem.submit()

"""
        browser.find_element_by_class_name(name)
        browser.find_elements_by_class_name(name)
        使用 CSS 类 name 的元素
        browser.find_element_by_css_selector(selector)
        browser.find_elements_by_css_selector(selector)
        匹配 CSS selector 的元素
        browser.find_element_by_id(id)
        browser.find_elements_by_id(id)
        匹配 id 属性值的元素
        browser.find_element_by_link_text(text)
        browser.find_elements_by_link_text(text)
        完全匹配提供的 text 的<a>元素
        browser.find_element_by_partial_link_text(text)
        browser.find_elements_by_partial_link_text(text)
        包含提供的 text 的<a>元素
        browser.find_element_by_name(name)
        browser.find_elements_by_name(name)
        匹配 name 属性值的元素
        browser.find_element_by_tag_name(name)
        browser.find_elements_by_tag_name(name)
        匹配标签 name 的元素
        (大小写无关，<a>元素匹配'a'和'A')
        tag_name 标签名，例如 'a'表示<a>元素
        get_attribute(name) 该元素 name 属性的值
        text 该元素内的文本，例如<span>hello</span>中的'hello'
        clear() 对于文本字段或文本区域元素，清除其中输入的文本
        is_displayed() 如果该元素可见，返回 True，否则返回 False
        is_enabled() 对于输入元素，如果该元素启用，返回 True，否则返回 False
        is_selected() 对于复选框或单选框元素，如果该元素被选中，选择 True，否则返回 False
        location 一个字典，包含键'x'和'y'，表示该元素在页面上的位置


"""




#发送特殊键
from selenium.webdriver.common.keys import Keys
"""
    Keys.DOWN, Keys.UP, Keys.LEFT,Keys.RIGHT 键盘箭头键
    Keys.ENTER, Keys.RETURN 回车和换行键
    Keys.HOME, Keys.END,
    Keys.PAGE_DOWN,Keys.PAGE_UP
    Home 键、End 键、PageUp 键和 Page Down 键
    Keys.ESCAPE, Keys.BACK_SPACE,Keys.DELETE Esc、Backspace 和字母键
    Keys.F1, Keys.F2, . . . , Keys.F12 键盘顶部的 F1到 F12键
    Keys.TAB Tab 键
    
    点击浏览器按钮
    利用以下的方法，selenium 也可以模拟点击各种浏览器按钮：
        browser.back()点击“返回”按钮。
        browser.forward()点击“前进”按钮。
        browser.refresh()点击“刷新”按钮。
        browser.quit()点击“关闭窗口”按钮。
"""

browser = webdriver.Firefox()
browser.get('https://www.baidu.com')
linkElem = browser.find_element_by_link_text('新闻')
linkElem.click()
htmlElem = browser.find_element_by_tag_name('html')
# htmlElem.send_keys(Keys.END) # scrolls to bottom
# htmlElem.send_keys(Keys.HOME) # scrolls to top

for i in range(10):
    browser.back()
    browser.forward()



