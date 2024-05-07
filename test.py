from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def ping():
    return "PONG !, HELLO FROM IBRAHIM"

def run():
  app.run(host='0.0.0.0',port=8780)

def server():
    t = Thread(target=run)
    t.start()
