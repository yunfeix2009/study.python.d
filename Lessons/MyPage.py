from flask_study.Flask import Flask
app = Flask(__name__)
@app.route("/")
def main_page():
    return 'Hello World'
if __name__=='__main__':
    app.run(debug=True)
