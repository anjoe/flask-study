from flask import Flask
from app01 import *
from app02 import *
from app03 import *

app = Flask(__name__)
app.register_blueprint(app01)
#app.register_blueprint(app01,url_prefix='/app01')
app.register_blueprint(app02)
#app.register_blueprint(app03,url_prefix='/app03')
#app.register_blueprint(app02,url_prefix='/app04')
#app.register_blueprint(app02)

@app.before_first_request
def before_freq():
    print("before_first_request_1")

@app.before_request
def before_req():
    print("before_request_1")

@app.teardown_request
def teardown_req(e):
    print("teardown_request")


if __name__=='__main__':
    app.run(host='0.0.0.0', port=80)

