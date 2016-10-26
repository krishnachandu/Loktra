from BeautifulSoup import BeautifulSoup
import re
from selenium import webdriver
keyword_to_be_searched="shoes"
class webScraper():
    def __init__(self,url):
        self.url=url
    def get_all_occurences_of_keyword(self,keyword):
        driver = webdriver.Chrome("C:\Users\KH2012\Downloads\chromedriver_win32\chromedriver.exe")#creating a chrome driver instance (custom path)
        driver.get(self.url)#Getting contents from webpage
        response = driver.page_source#getting page source to handle the dynamic html content
        response = response.text
        response = BeautifulSoup(response)
        result=response.findAll(text=re.compile(keyword, re.IGNORECASE))
        for i in range(len(result)):
            result[i]=str(result[i])
        return result
    def get_count_of_occurences_of_keyword(keyword,self):
        return len(self.get_all_occurences_of_keyword());

scraperObj=webScraper("http://www.shopping.com/")
print scraperObj.get_all_occurences_of_keyword(keyword_to_be_searched)
print scraperObj.get_count_of_occurences_of_keyword(keyword_to_be_searched);




