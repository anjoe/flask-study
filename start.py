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


if __name__=='__main__':
    app.run(host='0.0.0.0', port=80)

