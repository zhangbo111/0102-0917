import tornado.ioloop
import tornado.web
'''
tornado.web 是一个带有异步功能，并允许他扩展到大量的开放连接 简单web框架
'''


# 接口的处理类  继承处理接口的RequestHandler
class MainHandler(tornado.web.RequestHandler):

    # 定义get方法 处理get请求 不能携带参数
    # 不能处理除get以外的所有请求
    def get(self):
        # 使用write返回给前端页面数据（当前是字符串）
        # 可以方法html格式的字符串
        self.write("<h1>hello tornado</h1>")


if __name__ == "__main__":
    # 通过tornado.web创建一个Application对象
    # 第一个参数是匹配的路由地址 第二个参数是接口的处理类
    # 统一资源定位符： 协议名称：//域名.根域名/目录/文件名.后缀
    # "/"表示空目录， /tornado表示匹配tornado目录
    application = tornado.web.Application([
        (r"/tornado", MainHandler)
    ])
    # application对象监听端口
    application.listen(8888)
    print("server is start on 8888:")
    # 启动tornado服务
    tornado.ioloop.IOLoop.current().start()
