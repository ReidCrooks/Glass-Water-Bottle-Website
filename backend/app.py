from flask import Flask, render_template, jsonify, request
import sqlite3
import threading
from amazon_scraper import run_scraper

#Initizialize Flask app
app = Flask(__name__,
            static_folder='../frontend/static',
            template_folder='../frontend/templates')

#Connect to database
def get_db():
    conn = sqlite3.connect('backend/amazon_products.db')
    conn.row_factory = sqlite3.Row
    return conn


