#coding:utf-8

from selenium import webdriver
from time import sleep
def text_write(text_name,txt_p):
    local_file = open(text_name,'a')
    local_file.write(txt_p)
    local_file.write('\n')
    local_file.close()
#打开index
url_index = ('file:///C:/Users/Administrator/Desktop/xiaoshuo/index.htm')
#构造浏览器对象
chrome = webdriver.Chrome()
chrome.get(url_index)
#获取标题并转码为utf-8
#获取一共多少章节,并打开序章
all_num = len(chrome.find_elements_by_xpath('//div[8]//a'))
chrome.find_elements_by_xpath('//div[8]//a')[0].click()

#开始遍历章节
this_article_num=0
while this_article_num<all_num:
    # text_name =str(this_article_num)+'.txt'
    #获取标题并写入
    title_first = chrome.find_element_by_xpath('//h1')
    title_first = title_first.text
    text_name =title_first+'.txt'
    text_write(text_name,title_first.encode('utf-8'))
    this_article_num+=1
    #获取所有段落list
    p_tab = chrome.find_elements_by_xpath('//p')
    #开始遍历此章所有段落
    for p_one in p_tab:
        p_utf = p_one.text.encode('utf-8')
        text_write(text_name,p_utf)
    chrome.find_elements_by_xpath('//div[6]//div[2]//a')[0].click()