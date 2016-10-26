from BeautifulSoup import BeautifulSoup
import requests
import re
keyword_to_be_searched="shoes"
class webScraper():
    def __init__(self,url):
        self.url=url #constructing with url
    def get_all_occurences_of_keyword(self,keyword):
        response=requests.get(self.url);#Getting contents from webpage
        response=response.text
        response= BeautifulSoup(response)
        result=response.findAll(text=re.compile(keyword, re.IGNORECASE))
        for i in range(len(result)):
            result[i]=str(result[i])#converting unicode soup navigable strings
        return result
    def get_count_of_occurences_of_keyword(keyword,self):
        return len(self.get_all_occurences_of_keyword());

scraperObj=webScraper("http://www.shopping.com/")
print scraperObj.get_all_occurences_of_keyword(keyword_to_be_searched)


