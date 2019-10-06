from flask import Blueprint

app02=Blueprint('app02',__name__)

@app02.route('/02')
def show():
    return 'app01.hello'
