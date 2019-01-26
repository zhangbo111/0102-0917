import redis
import requests
from fake_useragent import UserAgent
from lxml import etree
import re
import json

# 1、连接redis数据库
r = redis.Redis(host="127.0.0.1", port="6379")

# 随机获取请求头
ua = UserAgent()
headers = {"User-Agent": ua.random}
# print(headers)
count = 1
count1 = 1
# 2、获取redis中的商圈分页url
business_circle_page_url_list = r.lrange("business_circle_page_url_list", 0, -1)
for business_circle_page_url in business_circle_page_url_list:

    print("==================第{}个页面下载==================".format(count1))

    # 将bytes类型解码为字符串
    business_circle_page_url = business_circle_page_url.decode("utf-8")
    # print(business_circle_page_url, type(business_circle_page_url))

    # 3、对商圈的分页url发起请求
    response = requests.get(business_circle_page_url, headers=headers)
    business_circle_page_html = response.text
    business_circle_page_html_xpath = etree.HTML(business_circle_page_html)

    # 4、获取每一套房源的信息列表
    house_info_list = business_circle_page_html_xpath.xpath("//div[@class='content__list']/div")
    # print(house_info_list, len(house_info_list))

    for house_info in house_info_list:
        # print(house_info, type(house_info))
        # 声明一个空字典 用于存放我们的房源信息
        house_info_dict = {}

        # 获取标题
        title = house_info.xpath(".//div[@class='content__list--item--main']/p[1]/a/text()")
        title = title[0].strip() if title else ""
        # print(title)
        house_info_dict["title"] = title

        # 获取城区
        city_area = house_info.xpath(".//div[@class='content__list--item--main']/p[2]/a[1]/text()")
        city_area = city_area[0].strip() if city_area else ""
        # print(city_area)
        house_info_dict["city_area"] = city_area

        # 获取商圈
        business_circle = house_info.xpath(".//div[@class='content__list--item--main']/p[2]/a[2]/text()")
        business_circle = business_circle[0].strip() if business_circle else ""
        # print(business_circle)
        house_info_dict["business_circle"] = business_circle

        # 获取价格
        house_price = house_info.xpath(".//span[@class='content__list--item-price']/em/text()")
        house_price = house_price[0].strip() if house_price else ""
        # print(house_price)
        house_info_dict["house_price"] = house_price

        # 获取房源面积
        room_info = house_info.xpath(".//p[@class='content__list--item--des']//text()")
        area = room_info[6].strip() if room_info else ""
        # print(area)
        house_info_dict["area"] = area

        # 获取朝向
        toward = room_info[8].strip() if room_info else ""
        # print(toward)
        house_info_dict["toward"] = toward

        # 获取房间个数
        fang_info = room_info[10].strip() if room_info else ""
        pattern1 = re.compile("\d")
        room = pattern1.match(fang_info).group()
        # print(room)
        house_info_dict["room"] = room

        # 获取厅的个数
        pattern2 = re.compile("(\d)厅")
        hall = pattern2.findall(fang_info)
        hall = hall[0] if hall else ""
        # print(hall)
        house_info_dict["hall"] = hall

        # 获取卫生间的个数
        pattern3 = re.compile("(\d)卫")
        toilet = pattern3.findall(fang_info)
        toilet = toilet[0] if toilet else ""
        # print(toilet)
        house_info_dict["toilet"] = toilet

        # 获取详情url
        detail_url = house_info.xpath(".//div[@class='content__list--item--main']/p[1]/a/@href")[0]
        detail_url = "https://bj.lianjia.com" + detail_url
        # print(detail_url)

        # 发情请求 获取详情页面信息
        response = requests.get(detail_url, headers=headers)
        detail_html = response.text
        detail_html_xpath = etree.HTML(detail_html)

        # 获取经纪人姓名
        agent_name = detail_html_xpath.xpath("//span[@class='contact_name']/@title")
        agent_name = agent_name[0] if agent_name else ''
        # print(agent_name)
        house_info_dict["agent_name"] = agent_name

        # 获取经纪人姓名
        # agent_phone = detail_html_xpath.xpath("//p[@class='content__aside__list--bottom oneline']/text()")
        # print(agent_phone)

        # 获取电话信息  //span[@class='content-right']/@data-event_action
        # https://bj.lianjia.com/zufang/aj/house/brokers?house_codes=BJ2157955625240772608&position=bottom&ucid=1000000020119607
        house_code = detail_html_xpath.xpath("//span[@class='content-right']/@data-event_action")
        house_code = house_code[0] if house_code else ''
        house_codes = house_code[11:]
        ucid = detail_html_xpath.xpath("//span[@class='contact__im']/@data-im_id")
        ucid = ucid[0] if ucid else ''
        # print(house_code)
        # print(ucid)

        phone_url = f"https://bj.lianjia.com/zufang/aj/house/brokers?house_codes={house_codes}&position=bottom&ucid={ucid}"
        # print(phone_url)
        response = requests.get(phone_url, headers=headers)
        agent_info_str = response.text
        # print(agent_info_str)
        phone_info = json.loads(agent_info_str)
        try:
            phone = phone_info.get("data", '').get(house_codes, '').get(house_codes, '').get("tp_number", '')
            # print(phone)
            house_info_dict["phone"] = phone
        except Exception as e:
            print(e)

        print(count, house_info_dict)
        count += 1
    count1 += 1
