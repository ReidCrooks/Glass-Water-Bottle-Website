from flask import Flask, render_template, jsonify, request
import sqlite3
import threading
#from amazon_scraper import run_scraper

#Initizialize Flask app
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
