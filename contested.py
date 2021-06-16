from flask import Flask, jsonify, request, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
from key import get_key
import os
import requests
import sqlite3

app = Flask(__name__)
#this value is not stored on github, change if you want to run your own local version
SECRET_KEY = get_key()
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/super_simple')
def super_simple():
    return SECRET_KEY

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
        return jsonify('try again'), 404
    return render_template('post.html', post=post)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    return post

if __name__ == '__main__':
    app.run()
