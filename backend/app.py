from flask import Flask, render_template, jsonify, request
import sqlite3
import threading
from amazon_scraper import run_scraper

