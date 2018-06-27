import redis
HOST = '127.0.0.1'
PORT = '6379'
DB = 0
pool = redis.ConnectionPool(host=HOST,port=PORT,db=DB)

def get_redis():
    pass