from services.handle import HandleImage
from flask import request, jsonify
from flask_restful import Resource

class ImageCloudinary(Resource):
    def __init__(self):
        self.handleImage = HandleImage()

    def post(self):
        uploadResponse = self.handleImage.upload(request)
        return jsonify(uploadResponse)
