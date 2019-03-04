"""
    Created by 朝南而行 2019/2/27 8:52
"""
import ast
import json


a = "start:{'time':'01','weather':'3'},{'time':'02','weather':'5'},{'time':'03','weather':'4'}"

new_a = a.replace('start:', '').split('},{')

city_weather = {}
city_weather_data = []
for x in range(0, len(new_a)):
    if new_a[x][0] != '{':
        new_a[x] = '{' + new_a[x]
    if new_a[x][-1] != '}':
        new_a[x] = new_a[x] + '}'

    city_weather_data.append(ast.literal_eval(new_a[x]))

city_weather['data'] = city_weather_data

# b = ast.literal_eval(city_weather['data'][0])

print(city_weather['data'][0]['time'])
