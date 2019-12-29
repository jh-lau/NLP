from celery import Celery
import time


broker = 'redis://172.17.0.6:6379'  # task send
backend = 'redis://172.17.0.6:6379' # results

app = Celery('task_demo', broker=broker, backend=backend)

@app.task
def add(x, y):
    time.sleep(2)
    return x + y

"""
分布式爬虫

step1: 

@app.task
def get_urls(url):
    pass
    send redis / result
    
@app.task
def get_page(url):
    pass 
    send redis / page
    
@app.task
def page_parse(page):
    pass
    send mongodb / page_content
          
Master:

   定义逻辑，发送任务
          
        
"""



