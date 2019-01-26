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
# 2、获取redis中的商圈url
business_circle_url_list = r.lrange("business_circle_url_list", 0, -1)
for c, business_circle_url in enumerate(business_circle_url_list):
    print("===============第{}个商圈开始下载==============".format(c + 1))

    # 将bytes类型解码为字符串
    business_circle_url = business_circle_url.decode("utf-8")
    # print(business_circle_url, type(business_circle_url))

    # 3、发起请求 获取商圈的页面的信息
    response = requests.get(business_circle_url, headers=headers)
    business_circle_html = response.text
    business_circle_html_xpath = etree.HTML(business_circle_html)

    # 获取商圈页面的最大页码
    business_circle_max_page = business_circle_html_xpath.xpath("//div[@class='content__pg']/@data-totalpage")
    # print(business_circle_max_page)
    if business_circle_max_page:
        # 提取商圈最大页码
        business_circle_max_page = int(business_circle_max_page[0])
    else:
        # 此商圈没有任何房源信息 跳过
        continue

    for page in range(business_circle_max_page):
        business_circle_page_url = business_circle_url + "pg{}/#contentList".format(page + 1)
        print(count, business_circle_page_url)
        count += 1
        # 将所有的商圈分页url添加到redis中
        r.lpush("business_circle_page_url_list", business_circle_page_url)



