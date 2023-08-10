from flask import Flask,redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world"

@app.route("/hey/<username>")
def hey_yingong(username):
    return "hey %s" % (username + username)

#自由插入数据类型
@app.route("/my/<float:number>")
def my_number(number):
    return "my %s" % (number + number)
#第二个百分号：格式化插值的方法

#可用性存疑
@app.route("/<username>/<float:number>")
def my_number_and_name(username,number):
    return "my %s" % (username + number)

#测试网页重定向：需要导入redirect包
@app.route("/jable")
def my_jable():
    return redirect("https://jable.tv/hot/")

app.run(host="0.0.0.0")
