from selenium import webdriver
import time

from tkinter import filedialog as fd
from tkinter import Tk



class Parse_follow:
    def __init__(self):
        self.root = Tk()
        self.webdriver_path = fd.askopenfilename()
        self.root.destroy()
        self.browser = webdriver.Chrome(self.webdriver_path)



    def logging(self):
        self.browser.get("https://hotline.ua")
        input = self.browser.find_element_by_xpath('//*[@id="searchbox"]')
        input.send_keys("rtx 3090")
        time.sleep(1.5)
        self.browser.find_element_by_xpath('//*[@id="doSearch"]').click()
        time.sleep(1.5)
        title = self.browser.find_element_by_xpath('//*[@id="page-catalog"]/div[1]/div[1]/div[1]/div[2]/aside/div/div[1]/div[1]/span[2]').text
        time.sleep(1.5)
        assert title == '15'
        like = self.browser.find_element_by_xpath('//*[@id="catalog-products"]/div/ul/li[1]/div[3]/ul/li[2]/span/span[2]').text
        assert like == 'Додати до списку'



parse_follow = Parse_follow()
parse_follow.logging()
