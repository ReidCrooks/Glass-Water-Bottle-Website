from flask import Flask, render_template
import os
#from amazon_scraper import run_scraper

#Initizialize Flask app
from flask import Flask, render_template

app = Flask(__name__, template_folder='frontend/templates', static_folder=os.path.abspath('static'))

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=5555,debug=True)
