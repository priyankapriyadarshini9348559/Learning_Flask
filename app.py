from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return "welcome to my first flask webapp"
@app.route('/about')
def about():
    return "i am learning Flask"
@app.route('/course')
def course():
    return "python Flask Development"
if __name__== '__main__':
    app.run(debug=True)