import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


class Scraping:
    def __init__(self, url,city):
        global file, browser
        self.url = url
        self.file_path = f"../datasets/" + str(city) + ".csv"
        self.file = open(self.file_path, "a", encoding="utf-8")
        col = ["City", "District", "Quarter", "Net m²", "Number of Rooms", "Building Age",
               "Floor Location", "Number of Floors",
               "Heating", "Number of Baths", "Balcony", "Furnished", "Price\n"]
        try:
            pd.read_csv(self.file_path)
        except pd.errors.EmptyDataError:
            self.file.write(",".join(col))
        browser = webdriver.Chrome()
        browser.implicitly_wait(3)
        browser.get(url)
        time.sleep(2)
        browser.refresh()
        time.sleep(1)
        close = browser.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        close.click()
        time.sleep(1)

    def scraping_data(self):
        try:
            self.elements = browser.find_elements(By.CLASS_NAME, 'classifiedInfoList')
            city = browser.find_element(By.XPATH, '//*[@id="classifiedDetail"]/div/div[2]/div[2]/h2/a[1]')
            town = browser.find_element(By.XPATH, '//*[@id="classifiedDetail"]/div/div[2]/div[2]/h2/a[2]')
            quarter = browser.find_element(By.XPATH, '//*[@id="classifiedDetail"]/div/div[2]/div[2]/h2/a[3]')
            self.file.write(city.text + "," + town.text + "," + " ".join(quarter.text.split(" ")[:-1]) + ",")
            price = browser.find_element(By.XPATH, '//*[@id="classifiedDetail"]/div/div[2]/div[2]/h3')
            values = [values.text for values in self.elements]
            info = " ".join(values).split("\n")[9:27:2]
            for data in info:
                self.file.write(data.strip() + ",")
            self.file.write(price.text.split(" ")[0].replace(".", ""))
            self.file.write("\n")
            browser.back()
        except:
            browser.back()

    def page_data(self, loops):
        for i in range(loops):
            try:
                ad_list = browser.find_elements(By.CLASS_NAME, "searchResultsItem     ")
                ad_list2 = list(
                    filter(lambda x: not x.get_attribute("class").__eq__("searchResultsItem nativeAd classicNativeAd")
                           , ad_list))
                ad_list2[i].click()
                self.scraping_data()
            except :
                print(f"{i} ilanda hata var")

    def program(self):
        loop = browser.find_element(By.XPATH,
                                    '//*[@id="searchResultsSearchForm"]/div/div[3]/div[1]/div[2]/div[1]/div/div['
                                    '1]/div/div[3]/span')
        page_numbers = int(loop.text.replace(" ilan", "").replace(".","")) // 20
        if page_numbers > 49 : page_numbers = 49
        for page in range(page_numbers + 1):
            number = browser.find_elements(By.CLASS_NAME, "searchResultsItem     ")
            edited_number = list(filter(lambda x: lambda x: not x.get_attribute("class").__eq__("searchResultsItem nativeAd classicNativeAd"), number))
            self.page_data(len(edited_number))
            try:
                next_button = browser.find_elements(By.CLASS_NAME, "prevNextBut")
                next_button[-1].click()
            except:
                pass
            time.sleep(2)
        browser.close()
        self.file.close()

    def close_file(self):
        self.file.close()
