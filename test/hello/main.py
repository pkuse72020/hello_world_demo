from flask import Flask,request,render_template,session,redirect,url_for,make_response,jsonify
import random
import keyword
import time

app=Flask("__name__")
app.config['SECRET_KEY'] = 'zkcpku'
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

@app.route("/")
def getRootHtml():
	return '<h1>Hello World!</h1>' + '<br> now time:' + str(time.time()) + '<br><br> Created using Flask.'

@app.route("/testPost",methods = ("POST",))
def testPostFunc():
	this_inp = request.form['inp']
	out_dict = {'inp':this_inp,'time':time.time(),'hello_msg':"hello world!"}

	return jsonify(out_dict)

@app.route("/testGet")
def testGetFunc():
	this_inp = 'test_get'
	out_dict = {'inp':this_inp,'time':time.time(),'hello_msg':"hello world!"}
	return jsonify(out_dict)

if __name__ == '__main__':
	app.jinja_env.auto_reload = True
	app.run(debug=True)


# python pdb 来自pytutor https://docs.python.org/3/library/pdb.html
# python code 可查阅文档https://docs.python.org/zh-cn/3.7/library/code.html#
# subprocess https://zhuanlan.zhihu.com/p/39079645
# exec
# byterun https://www.cnblogs.com/xyou/p/8861935.html https://github.com/nedbat/byterun


# https://blog.csdn.net/W_Meng_H/article/details/89399270 代码补全

# 当前的环境变量https://www.jb51.net/article/66439.htm

# print装饰https://www.jianshu.com/p/d485bb30c5bb
# 重定向https://www.cnblogs.com/zzhaolei/p/11068112.html
