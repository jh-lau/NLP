"""
  User: Liujianhan
  Time: 12:57
 """
__author__ = 'liujianhan'

from app import creat_app

app = creat_app()

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], port=app.config['PORT'])
