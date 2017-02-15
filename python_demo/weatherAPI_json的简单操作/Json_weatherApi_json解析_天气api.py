#coding:utf-8

import requests
import json

url = 'http://api.map.baidu.com/telematics/v3/weather?location=%E9%83%91%E5%B7%9E%E5%B8%82&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'
#获取json信息并得到一个json字典
def weather():    
    response = requests.get(url)
    dic_content = json.loads(response.content)
    return dic_content

#输出json信息
def print_json():
    dic = weather()
    if dic['status'] == 'success':
        dic_results_list = dic['results'][0]
        # print dic_results
        print '<><><><><><><><>'
        print '时间:',dic['date']
        print
        print '城市:' ,dic['results'][0]['currentCity']
        print 'pm2.5:',dic_results_list['pm25']
        print
        list_index = dic_results_list['index']
        index_num = 0
        print
        #迭代天气提示,输出提示信息
        print '<><>根据天气提示<><>'
        while index_num <len(list_index):
            print 
            print list_index[index_num]['title']
            print list_index[index_num]['zs']
            print list_index[index_num]['tipt']
            print list_index[index_num]['des']
            index_num+=1
        list_weather = dic_results_list['weather_data']
        print
        #迭代未来天气,输出天气信息
        print '<><>未来几天的天气<><>:'
        weather_num = 0
        while weather_num<len(list_weather):
            print
            print list_weather[weather_num]['date']
            print list_weather[weather_num]['dayPictureUrl']
            print list_weather[weather_num]['nightPictureUrl']
            print list_weather[weather_num]['weather']
            print list_weather[weather_num]['wind']
            print list_weather[weather_num]['temperature']
            weather_num+=1
print_json()