import textract
from FileReader import *
from flask import *
import pyrebase
import sys
app = Flask(__name__)
app.secret_key = 'some_secret'
config = {
    "apiKey": "AIzaSyBNeqANlaGZOcRX0aT_i1YfDbiCpTgfHqI",
    "authDomain": "flickering-fire-3792.firebaseapp.com",
    "databaseURL": "https://flickering-fire-3792.firebaseio.com",
    "projectId": "flickering-fire-3792",
    "storageBucket": "flickering-fire-3792.appspot.com",
    "messagingSenderId": "189921954509"
}
firebase = pyrebase.initialize_app(config)

@app.route('/', methods=['GET','POST'])
def start():
    session["user"] = None
    session["result"] = None
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            session["user"] = firebase.auth().sign_in_with_email_and_password(username, password)
            return redirect('/admin')
        except Exception as e:
            message = str(e)
            index = message.find("\"message\": \"")
            end = message.find("\"", index+12)
            print(index, end)
            error = message[index+12 : end]
            return render_template('login.html', error=error)
    else:
        if not session["user"]: 
            return render_template('login.html', error="")
        else:
            return redirect('/admin')

@app.route('/logout')
def logout():
    session["user"] = None
    return redirect('/login')


@app.route('/admin')
def admin():
    try:
        _ = session["user"]
    except Exception as e:
        session["user"] = None

    if session["user"] is None:
    # For testing only
        # user = "Test"
        # return redirect('/admin')
    # Actual line
        return redirect('/login')
    else:
        db = firebase.database()
        labels = [label.val() for label in db.child("Labels").get().each()]
        return render_template('admin.html', labels=labels)

@app.route('/reset-password', methods=["POST"])
def reset():
    email = request.form["username"]
    try:
        firebase.auth().send_password_reset_email(email)
        flash("Password reset email sent!")
    except Exception as e:
        message = str(e)
        index = message.find("\"message\": \"")
        end = message.find("\"", index+12)
        print(index, end)
        error = message[index+12 : end]
        flash(error)
    return redirect('/login')



@app.route('/main')
def main():
    try:
        _ = session["result"]
    except Exception as e:
        session["result"] = None

    return render_template('main.html')

@app.route('/result', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        data = request.form['text']
        if data == "":
            return redirect('/main')
        iconlist = FileReader.textSplit(data)

        db = firebase.database()
        labels = [label.val()["name"] for label in db.child("Labels").get().each()]
        for text, labelid in iconlist.items():
            iconlist[text] = labels[labelid]

        out = open("static/output.txt", "w+")
        for k in iconlist.keys():
            out.write("\n" + iconlist[k] + "\n" + "\n" + k + "\n" + "\n" + "----------" + "\n" + "\n")
        out.close()


        session["result"] = iconlist
        return render_template('result.html', result=iconlist)
    else:
        if session["result"]:
            return render_template('result.html', result=session["result"])
        else:
            return redirect('/main')


@app.route('/result-file', methods=['GET','POST'])
def analyzefile():
    if request.method == 'POST':
        f = request.files['file']
        text = textract.process(f.filename)
        iconlist = FileReader.fileSplit(text.decode('utf-8'))

        db = firebase.database()
        labels = [label.val()["name"] for label in db.child("Labels").get().each()]
        for text, labelid in iconlist.items():
            iconlist[text] = labels[labelid]

        out = open("static/output.txt", "w+")
        for k in iconlist.keys():
            out.write("\n" + iconlist[k] + "\n" + "\n" + k + "\n" + "\n" + "----------" + "\n" + "\n")
        out.close()

        session["result"] = iconlist
        return render_template('result.html', result=iconlist)
    else:
        if session["result"]:
            return render_template('result.html', result=session["result"])
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
    label = request.form['label']
    text = request.form['text']
    report(label, text)
    if session["result"]:
        return render_template('result.html', result=session["result"])
    else:
        return redirect('/main')


def report(label, text):
    db = firebase.database()
    db.child("Reports").push({"category":label, "text":text, "resolved":False})



@app.route('/userFeedback')
def feedback():
    try:
        _ = session["user"]
    except Exception as e:
        session["user"] = None

    if session["user"] is None:
    # For testing only
        # user = "Test"
        # return redirect('/userFeedback')
    # Actual line
        return redirect('/login')
    else:
        db = firebase.database()
        reports = []
        for key, report in [(item.key(), item.val()) for item in db.child('Reports').get().each()]:
                reports.append((key, report["category"], report["text"], report["resolved"]))
        return render_template('userFeedback.html', reports=reports)

@app.route('/edit-icon', methods=["POST"])
def editicon():
    name = request.form["name"]
    url = request.form["url"]
    desc = request.form["desc"]
    index = request.form["index"]

    if not url.endswith(".png") and not url.endswith(".jpg"):
        url = url + ".png"

    data = {
        "Labels/"+index: {
            "name" : name,
            "imgurl" : url,
            "description" : desc
        }
    }
    firebase.database().update(data)
    return redirect("/admin")


@app.route('/add-admin', methods=['POST'])
def add_admin():
    email = request.form['email']
    password = request.form['password']
    try:
        firebase.auth().create_user_with_email_and_password(email, password)
        flash("Account added successfully!")
    except Exception as e:
        message = str(e)
        index = message.find("\"message\": \"")
        end = message.find("\"", index+12)
        print(index, end)
        error = message[index+12 : end]
        flash(error)

    return redirect('/admin')

@app.route('/resolve', methods=['POST'])
def resolve():
    issueid = request.form['id']
    if not issueid:
        flash("No issue selected!")
    else:
        try:
            db = firebase.database()
            db.child("Reports").child(issueid).update({"resolved":True})
        except Exception as e:
            message = str(e)
            index = message.find("\"message\": \"")
            end = message.find("\"", index+12)
            print(index, end)
            error = message[index+12 : end]
            flash(error)

    return redirect('/userFeedback')

