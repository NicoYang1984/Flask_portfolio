from flask import Flask,redirect,request,jsonify,session

app = Flask(__name__)

@app.route("/")
def index():
    return "index"

#练习post：
@app.route("/post_test", methods=["POST"])
def post_test():
    my_json = request.get_json()
    #request是前端post上来的请求
    print(my_json)
    return jsonify(success=False, msg="参数不完整")
    #自己一开始学时没有弄返回值在里面，导致报错
    #python的函数都需要返回值

@app.route("/login", methods=["POST"])
def login():
    """
    账号 username asd123
    密码 password asdasd
    :return:
    """
    get_data = request.get_json()
    username = get_data.get("username")
    #获取键里面的值
    password = get_data.get("password")
    print(get_data)

    if not all([username, password]):
        return jsonify(success=False, msg="参数不完整")

    if username == "梁子洋" and password == "20030214YBC":
        # 如果验证通过 保存登录状态在session中
        # session["username"] = username
        #如果没有设置secret key的话，强行session会导致500 server error
        return jsonify(success=True,msg="登录成功")
    else:
        return jsonify(success=False,msg="账号或密码错误")


app.run(host="0.0.0.0", port=5001)
app.debug=True
#修改端口号有助于区别不同的flask应用
