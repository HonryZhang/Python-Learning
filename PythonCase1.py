#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
if __name__ == "__main__":

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
    driver = webdriver.Chrome(chrome_options=options)

    driver.implicitly_wait(3)

    driver.get("http://www.baidu.com")

    driver.find_element_by_id("kw").send_keys("hello Selenium!")

    driver.find_element_by_id("q").click()

    print 'Page title is:',driver.title

    driver.quit()