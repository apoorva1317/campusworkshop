"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7pdl269vf5qbacsjg-a.oregon-postgres.render.com",
        database="todo_g9ef",
        user="root",
        password="wqm1nOdrhJn3RtA2cAWg4KC46orIUd26")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
