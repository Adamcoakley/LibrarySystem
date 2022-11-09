from flask import Flask
from application import app

if app.name == "__main__":
    app.run(debug=True, host="0.0.0.0")
