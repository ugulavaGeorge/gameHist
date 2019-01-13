import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys

proxy_ip = "185.62.174.137:60613"
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy =  proxy_ip
capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)
page_address  = "http://csgofast.com/history/crash/all"
last_game = 0
colum_names = ["game_num", "hash", "salt", "number", "time", "multiplier"]
progress_file = "progress.txt"
driver_path = '/usr/lib/chromium-browser/chromedriver'
driver = webdriver.Chrome(executable_path = driver_path, desired_capabilities=capabilities)


def save_progress():
    return None


def get_hist():
    driver.get(page_address)
    elements = driver.find_elements_by_class_name("history-item crash")
    for i in range(5):
        elements[0].send_keys(Keys.ARROW_DOWN)
    for element in element:
        print(element.text)
    return None

get_hist()
    