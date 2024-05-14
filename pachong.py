import requests

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
p =  {"wd":"传智博客"}
url_temp = "https://www.baidu.com"
# response = requests.get("https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png")
r = requests.get(url_temp,headers=headers,params=p)
print(r.status_code)
print(r.request.url)

# with open("b.png","wb") as f:
#     f.write(response.content)