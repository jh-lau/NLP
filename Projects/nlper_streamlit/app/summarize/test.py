"""
  User: Liujianhan
  Time: 15:10
 """
__author__ = 'liujianhan'
import time
for i in range(1000):
    print("\r", f"{i}", end='', flush=True)
    time.sleep(.01)