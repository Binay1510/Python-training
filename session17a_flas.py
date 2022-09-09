from flask import *

web_app=Flask("HealthLogger")
print(web_app)

@web_app.route("/")    #decorater
def index():

    #return "Welcome to Health Logger"
    #return html_content
    return render_template("index.html")

@web_app.route("/login")
def login():
    return render_template("login.html")

@web_app.route("/register")
def register():

    return render_template("register.html")
    #return "You can Register in  the app "


@web_app.route("/logs")
def logs():
    return render_template("logs.html")

@web_app.route("/logger")
def logger():
    return render_template("logger.html")

def main():
    web_app.run()
if __name__=="__main__":
        main()