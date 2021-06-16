from flask import Flask
from threading import Thread

app = Flask('DevHeat Beta')

@app.route('/')
def home():
  return "<h1>I am alive</h1>"

def run():
  app.run(host='0.0.0.0')

def keep_alive():
  t = Thread(target=run)
  t.start()