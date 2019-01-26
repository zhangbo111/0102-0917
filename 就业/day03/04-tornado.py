import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    # 使用get方法获取的时候 返回的内容
    def get(self):
        self.write("Hello, world")


# 监听本地主机 第二个参数的触发的类
application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    # 监听指定端口
    application.listen(8888)
    # 启动
    tornado.ioloop.IOLoop.instance().start()



