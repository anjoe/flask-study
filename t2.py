
from t import app

@app.route('/time2',methods=['post','get'])
def get_time2():
    return 't'
