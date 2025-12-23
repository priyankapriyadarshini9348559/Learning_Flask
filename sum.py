from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return "Igonre this page or see it (choice is yours)"
@app.route('/add/<int:a>/<int:b>')
def add(a,b):
    return f"sum is {a+b}"
if __name__ == '__main__':
    app.run(debug=True)