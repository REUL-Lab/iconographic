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
saved_result = None

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
        labels = [label.val() for label in db.child("Labels").get().each()]
        imgurls = ["https://REUL-Lab.github.io/iconographic/images/"+label+".png" for label in labels]
        return render_template('admin.html', labels=zip(labels,imgurls))

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/result', methods=['GET', 'POST'])
def analyze():
    global saved_result
    if request.method == 'POST':
        data = request.form['text']
        if data == "":
            return redirect('/main')
        iconlist = FileReader.textSplit(data)

        db = firebase.database()
        labels = [label.val() for label in db.child("Labels").get().each()]
        for text, labelid in iconlist.items():
            iconlist[text] = labels[labelid]

        out = open("output.txt", "w+")
        for k in iconlist.keys():
            out.write(iconlist[k] + "\n" + k + "----------")
        out.close()

        saved_result = iconlist
        return render_template('result.html', result=iconlist)
    else:
        if saved_result:
            return render_template('result.html', result=saved_result)
        else:
            return redirect('/main')


@app.route('/result-file', methods=['GET','POST'])
def analyzefile():
    global saved_result
    if request.method == 'POST':
        f = request.files['file']
        if f:
            text = str(f.read(), 'utf-8')
            iconlist = FileReader.fileSplit(text)

            db = firebase.database()
            labels = [label.val() for label in db.child("Labels").get().each()]
            for text, labelid in iconlist.items():
                iconlist[text] = labels[labelid]

            out = open("output.txt", "w+")
            for k in iconlist.keys():
                out.write(iconlist[k] + "\n" + k + "----------")
            out.close()


            saved_result = iconlist
            return render_template('result.html', result=iconlist)
    else:
        if saved_result:
            return render_template('result.html', result=saved_result)
        else:
            return redirect('/main')

@app.route('/report-main', methods=['POST'])
def report_main():
    label = request.form['label']
    text = request.form['text']
    report(label, text)
    return redirect('/main')

@app.route('/report-result', methods=['POST'])
def report_result():
    global saved_result
    label = request.form['label']
    text = request.form['text']
    report(label, text)
    if saved_result:
        return render_template('result.html', result=saved_result)
    else:
        return redirect('/main')


def report(label, text):
    db = firebase.database()
    db.child("Reports/"+label).push(text)



@app.route('/userFeedback')
def feedback():
    global user
    if user is None:
        return redirect('/login')
    else:
        db = firebase.database()
        reports = []
        for category in [label.key() for label in db.child('Reports').get().each()]:
            for report in [item.val() for item in db.child('Reports/'+category).get().each()]:
                reports.append((category, report))
        return render_template('userFeedback.html', reports=reports)

@app.route('/editicon')
def editicon():
    global user
    if user is None:
        return redirect('/login')
    else:
        return render_template('editicon.html')