from FileReader import *
from flask import *
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def start():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/admin', methods=['GET','POST'])
def admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # check w/ db
    return render_template('admin.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/result', methods=['GET', 'POST'])
def analyze():

    fr = FileReader()
    if request.method == 'POST':
        data = request.form['text']
        if data == "":
            return render_template('result.html', result=["Placeholder"])
        # do shit with data
        iconlist = FileReader.textSplit(data)
        return render_template('result.html', result=iconlist)
    else:
        return render_template('result.html', result=["Placeholder"])


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