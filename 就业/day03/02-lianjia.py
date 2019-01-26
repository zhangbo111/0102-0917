import redis
import requests
from fake_useragent import UserAgent
from lxml import etree
import re

# 1、连接redis数据库
r = redis.Redis(host="127.0.0.1", port="6379")

# 随机获取请求头
ua = UserAgent()
headers = {"User-Agent": ua.random}
# print(headers)

count = 1
# 2、从redis数据库的中获取所有的城区url
city_area_url_list = r.lrange("city_area_url_list", 0, -1)
for city_area_url in city_area_url_list:

    # 从redis数据库当中获取的数据是bytes类型
    # print(city_area_url, type(city_area_url))
    # 将bytes类型数据解码为字符串
    city_area_url = city_area_url.decode("utf-8")
    # print(city_area_url, type(city_area_url))

    # 获取url当中的城区信息
    pattern = re.compile("zufang/(.*?)/")
    city_area = pattern.findall(city_area_url)[0]
    print('=================={}下载开始===================='.format(city_area))

    # 3、对所有的城区url发起请求
    # 只用通过城区url才能获取到商圈url
    response = requests.get(city_area_url, headers=headers)
    city_area_html = response.text
    # print(city_area_html)
    # 生成一个xpath对象
    city_area_html_xpath = etree.HTML(city_area_html)
    # print(city_area_html)

    # 4、获取所有的城区对应的所有商圈url
    business_circle_url_list = city_area_html_xpath.xpath("//div[@id='filter']/ul[4]/li[position()>1]/a/@href")
    # print(business_circle_url_list)

    # 5、拼接完整的商圈url
    for business_circle_url in business_circle_url_list:
        business_circle_url_full = "https://bj.lianjia.com" + business_circle_url
        print(count, business_circle_url_full)

        # 6、将所有的城区对应的所有商圈url添加进入到redis数据库
        r.lpush("business_circle_url_list", business_circle_url_full)
        count += 1
