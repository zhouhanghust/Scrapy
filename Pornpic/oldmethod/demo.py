from bs4 import BeautifulSoup
import requests



headers = {
'Host':'www.mm131.com',
'Cookie':'UM_distinctid=168e7290c8259e-01d7711b72021e-10346654-1fa400-168e7290c8343e; CNZZDATA3866066=cnzz_eid%3D193397086-1494676185-%26ntime%3D1494676185; bdshare_firstime=1550066453750; Hm_lvt_9a737a8572f89206db6e9c301695b55a=1550066454; Hm_lpvt_9a737a8572f89206db6e9c301695b55a=1550154092',
'Referer':'http://www.mm131.com/xinggan/4765_7.html',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


url = "http://www.mm131.com/xinggan/4765_6.html"
res = requests.get(url,headers=headers)

soup = BeautifulSoup(res.text,'lxml')
result = soup.select('div.content div.content-pic a img')[0]["src"]
print(result)

pic = requests.get(result)
if pic.status_code == 200:
    with open("./xxx.jpg", "wb") as f:
        f.write(pic.content)




