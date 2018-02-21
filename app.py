from FileReader import *
from flask import *
import pyrebase
import sys
app = Flask(__name__)
config = {
    "apiKey": "AIzaSyBNeqANlaGZOcRX0aT_i1YfDbiCpTgfHqI",
    "authDomain": "flickering-fire-3792.firebaseapp.com",
    "databaseURL": "https://flickering-fire-3792.firebaseio.com",
    "projectId": "flickering-fire-3792",
    "storageBucket": "flickering-fire-3792.appspot.com",
    "messagingSenderId": "189921954509"
}
firebase = pyrebase.initialize_app(config)
user = None

@app.route('/', methods=['GET','POST'])
def start():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    global user
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            user = firebase.auth().sign_in_with_email_and_password(username, password)
            return redirect('/admin')
        except Exception as e:
            return render_template('login.html', error=e)
    else:
        if user is None:
            return render_template('login.html', error="")
        else:
            return redirect('/admin')

@app.route('/logout')
def logout():
    global user
    user = None
    return redirect('/login')

@app.route('/admin')
def admin():
    global user
    if user is None:
        return redirect('/login')
    else:
        db = firebase.database()
        labels = db.child("labels").get().val()
        return render_template('admin.html', labels=labels)

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/result', methods=['GET', 'POST'])
def analyze():

    if request.method == 'POST':
        data = request.form['text']
        if data == "":
            return redirect('/main')
        # do shit with data
        iconlist = FileReader.textSplit(data)
        print(iconlist)
        return render_template('result.html', result=iconlist)
    else:
        return redirect('/main')


@app.route('/result-file', methods=['POST'])
def analyzefile():
    
    f = request.files['file']
    if f:
        text = str(f.read(), 'utf-8')
        iconlist = FileReader.fileSplit(text)
        return render_template('result.html', result=iconlist)

@app.route('/userFeedback')
def feedback():
    return render_template('userFeedback.html')


@app.route('/reports')
def reports():
    return render_template('reports.html')

    
@app.route('/editicon')
def editicon():
    return render_template('editicon.html')