import redis
r = redis.Redis(host='127.0.0.1',port=6379,db=0,decode_responses=True)

# print r.exists('hset1')
# r.hmset('hset1',{'k1':'v1','k2':'v2'})
print r.exists('hset1')
print r.hget('hset1','k1')