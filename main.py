from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Userinfo import email,password
import time

class YTNK:
  def __init__(self,email,password):
    self.browser = wd.Chrome()
    self.email = email
    self.password = password
    self.Link_list = []
    self.login()

  def login(self):
    self.browser.get("https://ytnk.tv/")
    time.sleep(2)
    self.browser.find_element(By.XPATH,'//*[@id="header"]/div/a').click()
    time.sleep(1)
    emailInput = self.browser.find_element(By.XPATH,'//*[@id="TxtEposta"]')
    passwordInput= self.browser.find_element(By.XPATH,'//*[@id="TxtSifre"]')
    emailInput.send_keys(self.email)
    passwordInput.send_keys(self.password)
    enterSite = self.browser.find_element(By.XPATH,'//*[@id="ytnktv"]/div[2]/button')
    enterSite.click()
    time.sleep(2)
    self.goVideos()
  
  def goVideos(self):
    self.browser.get("https://ytnk.tv/egitim-detay/kariyer-planlama-dersi/3FF644FE-874B-4EC2-8E14-768F7B304356")
    time.sleep(1)
    self.browser.find_element(By.XPATH,"/html/body/main/div[1]/div[2]/div/div[2]/div/div[3]/a").click()
    time.sleep(1)
    self.getLinks()
    for link in self.Link_list[1:]:
      self.browser.get(link)
      self.WatchVideo()

  def getLinks(self):
    with open("urls.txt","r",encoding="utf-8") as file:
      self.Link_list = file.readlines()

  def WatchVideo(self):
    time.sleep(0.5)  
    self.browser.find_element(By.XPATH,'//*[@id="YtnkPlayer"]/button').click()
    time.sleep(0.5)
    self.browser.find_element(By.XPATH,'//*[@id="YtnkPlayer"]/div[4]/div[1]/button').click()
    while True:
      videoTime = self.browser.find_element(By.XPATH,'//*[@id="YtnkPlayer"]/div[4]/div[7]/span[3]').text
      print(videoTime)
      time.sleep(1)
      self.browser.find_element(By.XPATH,'//*[@id="YtnkPlayer"]/div[4]/div[12]/button').click()
      if videoTime == "0:03": 
        break
    time.sleep(5)
    self.browser.find_element(By.XPATH,'/html/body/div[7]/div/div[4]/div[1]/button').click()

ytnktv = YTNK(email,password)
num = 0
while True:
  if num == 0:
   ytnktv()
  else:
    continue
  num += 1
