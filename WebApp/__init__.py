from flask import Flask
app = Flask(__name__)
from WebApp import routes

def alam():
    mafla = 0
    apro = 0
    anyoka = mafla + apro
    return 0