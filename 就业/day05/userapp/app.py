import tornado.web
import tornado.ioloop
import tornado.httpserver
from handlers import user as user_handlers


# 定义全局的HANDLERS
# 第一个参数使用正则匹配
# 会把括号里面的数据进行传递
HANDLERS = [
    (r"/api/users/(\d+)", user_handlers.UserHandler),
    (r"/api/users", user_handlers.UserListHandler)
]

def run():

    # 创建一个application对象
    app = tornado.web.Application(
        HANDLERS,
        debug=True  # 表示修改之后自动重启
    )
    # 连接非阻塞的tornado服务器
    http_server = tornado.httpserver.HTTPServer(app)
    port = 8080
    # 监听端口
    http_server.listen(port)
    print("server is start on {}:".format(port))
    # 启动服务
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    run()


