from flask import Blueprint

app03=Blueprint('app03',__name__)

@app03.route('/t3/')
def show():
    return 'app03.hello'
