import os
import cloudinary.uploader as uploadToCloudinary
from cloudinary import cloudinary, CloudinaryImage
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load Cloudinary configuration from environment variables
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

class HandleImage():
    def upload(self, request):
        # Get the image file from the request
        image = request.form.get("url") or request.files.get("file")

        # Upload the image to Cloudinary
        response = uploadToCloudinary.upload(image)

        # Extract the public_id and url from the response
        publicId = response.get("public_id")
        url = response.get("secure_url")
        return {'public_id': publicId, 'format': format, 'url_upload': url}



    def transformation(self, imageCloudinary, request):
        width = request['width']
        height = request['height']

        cloudinaryImage = CloudinaryImage(imageCloudinary['public_id'])
        cloudinaryImage.resize(crop='fill', width=width, height=height)
