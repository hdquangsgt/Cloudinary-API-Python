from services.download import DownloadFile
from services.handle import HandleImage
from flask import request, jsonify
from flask_restful import Resource

class HandleCloudinary(Resource):
    def __init__(self):
        self.downloadFile = DownloadFile()
        self.handleImage = HandleImage()

    def post(self):
        uploadResponse = self.handleImage.upload(request)
        self.handleImage.transformation(uploadResponse, request)
        
        urlImage = self.downloadFile.downloadImage(uploadResponse['url_upload'], uploadResponse['public_id'])

        return jsonify({"message": 'Handle image completed', "url": urlImage})