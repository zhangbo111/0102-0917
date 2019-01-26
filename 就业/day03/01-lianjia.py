'''
需求：抓取链家（北京）各地区租房信息，并按照指定的字段，格式存入mysql数据库
项目分析：我们要达到的目的是抓取北京链家租房的所有房屋信息，并且每天凌晨2:00抓取一次
下午18：00抓取一次，为了保证每天都有北京链家租房数据更新，我们写了监控，监控数据库数据的每日更新量
如果低于80%，则使用邮件报警提示负责人检查爬取过程是否有问题？
一般的问题有:1、网站更新，xpath失效，  2、抓取的url变更 3、其他

抓取策略:想要完整的抓取的北京链家租房信息，因为北京租房的url：https://bj.lianjia.com/zufang
只能抓取3000条信息，但是网站上面有16000左右，通过https://bj.lianjia.com/zufang不能抓取到所有数据
解决方案：通过https://bj.lianjia.com/zufang获取城区的url信息，再通过城区的url信息，抓取商圈的url信息，
我们抓取的流程是先抓取每套房源url，存入缓存数据库redis，然后再通过url获取每套房源的详细信息。
获取的详细信息有：room，price...
'''
# 1、抓取城区的url（大概有18个城区url）
import requests
from fake_useragent import UserAgent
import redis
from lxml import etree

# 1、连接本地redis数据库 用于存储url
r = redis.Redis(host='127.0.0.1', port='6379')
# print(r.keys())
# print(r.get("cloth"))
# print(r.get("addr"))
# print(r.get("hair"))

# 生成UserAgent对象
ua = UserAgent()

# 生成请求头 随机获取请求头对象
headers = {"User-Agent": ua.random}
# print(headers)

# 2、发起请求
base_url = "https://bj.lianjia.com/zufang/"
response = requests.get(base_url, headers=headers)
# print(response.text)
zufang_html = response.text
# 转换为etree对象  可以使用xpath
zufang_html = etree.HTML(zufang_html)
# print(zufang_html, type(zufang_html))
# 3、xpath获取每个区域的url
city_area_url_list = zufang_html.xpath("//div[@id='filter']/ul[2]/li[position()>1]/a/@href")
# print(city_area_url_list)

# 4、循环拼接完整的url信息
for city_area_url in city_area_url_list:
    # print(city_area_url)
    city_area_url_full = "https://bj.lianjia.com" + city_area_url
    print(city_area_url_full)

    # 5、将url存入redis数据库
    r.lpush("city_area_url_list", city_area_url_full)
