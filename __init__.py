from flask import  Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "hello"

@app.route('/home')
def home2():
    return 'hello2'

if __name__ == "__main__":
        print("Hello world")
        #app.run()
