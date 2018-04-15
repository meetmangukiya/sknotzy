from flask import Flask

app = Flask(__name__)

@app.route('/')
def sknotzy():
    return "Hey, this is sknotzy"

if __name__ == '__main__':
    app.run()
