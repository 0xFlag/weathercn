#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import re

def weatherNow():
	a = input("请输入查询天气格式（天气 地名）：")
	if a == "":
		print("请输入天气地名")
	elif "天气" in a:
		url = "https://www.tianqiapi.com/api/?version=v6&city="
		b = a.strip("天气")
		r='[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+' # 正则删除标点符号
		c=re.sub(r,'',b)
		post = c.strip(" ") # 删除空格
		#print(post) # 测试
		url_now = url + post
		rs_we = requests.get(url_now).json()
		weather_city = rs_we["city"]
		if weather_city == post:
			weather_uptime = rs_we["date"] + "\000" + rs_we["week"] + "\000" + rs_we["update_time"] # 更新时间
			weather_wea = rs_we["wea"] # 天气情况
			weather_tem = rs_we["tem"] + "℃" # 当前温度
			weather_temnow = rs_we["tem2"] + "/" + rs_we["tem1"] + "℃" # 早晚温差
			weather_win = rs_we["win"] # 风向
			weather_win_speed = rs_we["win_speed"] # 风速等级
			weather_win_meter = rs_we["win_meter"] # 风速
			weather_humidity = rs_we["humidity"] # 湿度
			weather_visibility = rs_we["visibility"] # 能见度
			weather_pressure = rs_we["pressure"] + "hPa" # 气压
			weather_air = rs_we["air"] # 空气质量
			weather_air_pm25 = rs_we["air_pm25"] # PM2.5
			weather_air_level = rs_we["air_level"] # 空气质量等级
			print(weather_city + "-今日天气预报（实时）：" + "\r\n当前温度：" + weather_tem + "\r\n早晚温差：" + weather_temnow + "\r\n天气情况：" + weather_wea + "\r\n湿度：" + weather_humidity + "\r\n空气质量：" + weather_air + "\r\nPM2.5：" + weather_air_pm25 + "\r\n空气质量等级：" + weather_air_level + "\r\n气压：" + weather_pressure + "\r\n风向：" + weather_win + "\r\n风速：" + weather_win_meter + "\r\n风速等级：" + weather_win_speed + "\r\n能见度：" + weather_visibility + "\r\n更新时间：" + weather_uptime)
		else:
			print("当前地区无法查询天气")
	else:
		print("查询格式错误")

def weatherWeek():
	a = input("请输入查询天气格式（天气预报 地名）：")
	if a == "":
		print("请输入天气预报地名")
	elif "天气预报" in a:
		url = "https://www.tianqiapi.com/api/?version=v1&city="
		b = a.strip("天气预报")
		r='[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+' # 正则删除标点符号
		c=re.sub(r,'',b)
		post = c.strip(" ") # 删除空格
		print(post)
		url_now = url + post
		rs_we = requests.get(url_now).json()
		weather_city = rs_we["city"]
		if weather_city == post:
			print(weather_city + "-一周天气预报（3小时更新一次）：")
			for x in range(0,7):
				weather_day = rs_we["data"][x]["day"] # 日期
				weather_date = rs_we["data"][x]["date"] # 年月日
				weather_week = rs_we["data"][x]["week"] # 星期
				weather_datetime = weather_date + "\000" + weather_week + "\000" + weather_day

				weather_wea = rs_we["data"][x]["wea"] # 天气情况
				#weather_air = rs_we["data"][0]["air"] # 空气质量
				#weather_humidity = rs_we["data"][0]["humidity"] # 湿度
				#weather_air_level = rs_we["data"][0]["air_level"] # 空气质量等级
				weather_tem = rs_we["data"][x]["tem"] # 温度
				weather_temnow = rs_we["data"][x]["tem2"] + "/" + rs_we["data"][x]["tem1"] # 早晚温差
				weather_win = rs_we["data"][0]["win"][0] + "/" + rs_we["data"][0]["win"][1] # 早晚风向
				weather_win_speed = rs_we["data"][0]["win_speed"] # 风速
				#weather_uptime = "更新时间：" + rs_we["update_time"] # 更新时间
				
				# 指数
				# uvi 紫外线指数
				weather_uvi = rs_we["data"][x]["index"][0]["title"] + "：" + rs_we["data"][x]["index"][0]["level"] + "\r\n" + rs_we["data"][x]["index"][0]["desc"]
				# sport 运动指数
				weather_sport = "运动指数：\r\n" + rs_we["data"][x]["index"][1]["desc"]
				# blood 健臻·血糖指数
				weather_blood = rs_we["data"][x]["index"][2]["title"] + "：" + rs_we["data"][x]["index"][2]["level"] + "\r\n" + rs_we["data"][x]["index"][2]["desc"]
				# clothe 穿衣指数
				weather_clothe = rs_we["data"][x]["index"][3]["title"] + "：" + rs_we["data"][x]["index"][3]["level"] + "\r\n" + rs_we["data"][x]["index"][3]["desc"]
				# washcar 洗车指数
				weather_washcar = rs_we["data"][x]["index"][4]["title"] + "：" + rs_we["data"][x]["index"][4]["level"] + "\r\n" + rs_we["data"][x]["index"][4]["desc"]
				# air 空气污染扩散指数
				weather_air = rs_we["data"][x]["index"][5]["title"] + "：" + rs_we["data"][x]["index"][5]["level"] + "\r\n" + rs_we["data"][x]["index"][5]["desc"]
				# index 天气指数合并
				weather_index = weather_uvi + "\r\n\r\n" + weather_sport + "\r\n\r\n" + weather_blood + "\r\n\r\n" + weather_clothe + "\r\n\r\n" + weather_washcar + "\r\n\r\n" + weather_air
				# mes 天气预报合并
				weather_mes = weather_datetime + "\r\n温度：" + weather_tem + "\r\n早晚温差：" + weather_temnow + "\r\n天气情况：" + weather_wea + "\r\n早晚风向：" + weather_win + "\r\n风速：" + weather_win_speed + "\r\n"

				weather_info = weather_mes + weather_index + "\r\n" + "-----"*6
				
				print(weather_info)
				
			weather_uptime = "更新时间：" + rs_we["update_time"]
			print(weather_uptime)
		else:
			print("当前地区无法查询天气预报")
	else:
		print("查询格式错误")


if __name__ == '__main__':
	while True:
		print('1.天气查询')
		print('2.天气预报查询')
		num = input('>>> 输入查询编号 1-2: ')
		print('------'*6)
		if num == '1':
			weatherNow()
			break
		elif num == '2':
			weatherWeek()
			break