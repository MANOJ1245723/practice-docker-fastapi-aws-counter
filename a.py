from fastapi import FastAPI
import redis
app = FastAPI()
r = redis.Redis(host='redis', port=6379, decode_responses=True)
@app.get('/')
def get_data():
    r.incr('visited')
    value = r.get('visited')
    return {'visited': int(value), 'message':'hello'}