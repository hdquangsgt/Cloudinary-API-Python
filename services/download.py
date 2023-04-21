def download_image(request):
    # Get the URL of the image from the request
    url = request.form.get('url')

    # Make a request to the URL and get the image data
    response = requests.get(url)
    image_data = response.content

    # Define the path where you want to save the image
    path = os.path.join('storage', 'image', 'image.jpg')

    # Save the image data to a file in the specified path
    with open(path, 'wb') as file:
        file.write(image_data)

    return 'Image downloaded and saved successfully'