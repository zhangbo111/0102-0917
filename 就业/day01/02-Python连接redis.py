# Python连接redis
import redis
r = redis.Redis(host="127.0.0.1", port="6379")
print(r, type(r))
result = r.get("addr")
print(result)

