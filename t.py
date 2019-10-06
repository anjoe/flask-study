import flask
import datetime

app=flask.Flask(__name__)

@app.route('/time',methods=['post','get'])
def get_time():
    now=str(datetime.datetime.now())
    return "当前的时间是：%s"%now

@app.route('/',methods=['post','get'])
def index_():
    now=str(datetime.datetime.now())
    return "当前的时间是：%s"%now

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s!<h1>'%name

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
