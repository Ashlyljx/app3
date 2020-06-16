from flask import Flask,render_template ###render_template will access html file in teh python, and change it to url, which can be accessed public

##create a new folder (must named "templates", in this folder,create  a new file, called templates\home.html

###name 两边的——比较长，可以打两个下划线，或者根据atom自动跳出来的符号
app=Flask(__name__, template_folder="templates")

##@app.route("/")要紧跟在后面define的function后面，并且要一起跑，否则会报错
@app.route('/')   ###如果改成@app.route('/about/') ,那么访问的地址就会变成http://127.0.0.1:5000/about/
def home():
    return render_template("home.html")

##create a new page
@app.route('/project')
def project():
    return render_template("project.html")

@app.route('/project1')
def project():
    return render_template("project1.html")

##create a new page
@app.route('/about')   ###如果改成@app.route('/about/') ,那么访问的地址就会变成http://127.0.0.1:5000/about/
def about():
    return render_template("about.html")

@app.route('/contact')
def project():
    return render_template("contact.html")


##全部运行完code之后，output中会显示网址。但是这个是localhost，只有这台电脑能够访问
if __name__ =="__main__":
    app.run(debug=False)

###一直运行都不行，卧槽，关闭了所有文件重开了atom，又可以了.还有一种可能是py文件和templates放在一个文件夹里面，并且只有这个文件夹，而不是把整个download文件夹导入
