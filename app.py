from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

if __name__ == '__main__':
    #127.0.0.1:8000
    app.run(debug=True, port=8000)
