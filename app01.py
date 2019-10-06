from flask import Blueprint
from flask import redirect,abort,request,render_template

app01=Blueprint('app01',__name__,template_folder='pages')

@app01.route('/01')
def redirect():
    return redirect('http://www.baidu.com')

@app01.route('/abort')
def test():
	return abort(404)

@app01.route('/user/<name>')
def user_name(name):
	print(request.method) #获取访问方式 GET
	print(request.url) #获取url http://127.0.0.1:5000/req?id=1&name=wl
	print(request.cookies) #获取cookies {}
	print(request.path)  # 获取访问路径 /req
	print(request.args) #获取url传过来的值  ImmutableMultiDict([('id', '1'), ('name', 'wl')])
	print(request.args.get("test")) #get获取id  1
	print(request.args["test"]) # 索引获取name wl
	print(request.args.to_dict()) # 获取到一个字典 {'id': '1', 'name': 'wl'}

	return name

@app01.route('/tpl2/<name>')
def stp2(name):
    my_str = 'Hello Word'
    my_int = 10
    return render_template("t2.html",a=my_str,b=my_int,name=name)

@app01.route('/tpl/<int:name>')
def stpl(name):
    my_str = 'Hello Word'
    my_int = 10
    return render_template("tpl.html",a=my_str,b=my_int,c=name)

