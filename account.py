from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return "welcome to my bankaccount"
@app.route('/account/<name>/<int:amount>')
def account(name,amount):
    return f"account_holder_name:{name},total amount available:{amount}"
if __name__== '__main__':
    app.run(debug=True)