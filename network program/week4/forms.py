import imp
from urllib import response


import requests

data_dictionary = {'custome': 'martin', 'cuttel': '32232', 'size': 'large'}

response = requests.post("http://httpbin.org/post", data=data_dictionary)
print("HTTP Status Code : " + str(response.status_code))
if response.status_code == 200:
    print(response.text)