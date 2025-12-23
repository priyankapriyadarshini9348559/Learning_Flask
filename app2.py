from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return "Home page is working"
@app.route('/check/<int:num>')
def check(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
if __name__ == '__main__':
    app.run(debug=True)