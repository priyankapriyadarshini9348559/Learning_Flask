from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return "just see this"
@app.route('/student/<name>/<int:marks>')
def student(name,marks):
    return f"student Name:{name},Marks:{marks}"
if __name__ == '__main__':
    app.run(debug=True)