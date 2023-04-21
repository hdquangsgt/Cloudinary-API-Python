from flask import Flask
from flask_restful import Resource, Api
from routes import 'routes/api.py'

app = Flask(__name__)
api = Api(app)

api.add_resource(UploadImage, "/upload")

if __name__ == '__main__':
    app.run()
