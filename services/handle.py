from flask import request, jsonify

class HandleImage():
    def post(self):
         # Get the image file from the request
        image = request.files.get("image")

        # Upload the image to Cloudinary
        response = cloudinary.uploader.upload(image)
        
        # Extract the public_id and url from the response
        public_id = response.get("public_id")
        url = response.get("url")

        # Return the public_id and url in the JSON response
        return jsonify({"public_id": public_id, "url": url})