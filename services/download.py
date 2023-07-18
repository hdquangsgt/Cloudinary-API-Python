import os
import requests
from flask import request

class DownloadFile:
    def downloadImage(self, url, fileName = 'image.jpg'):
        extendtion = '.jpg'
        file = fileName + extendtion
        folderName = 'upload'
        r = requests.get(url, stream = True)
        completeName = os.path.join(folderName, file)

        open(completeName, 'wb').write(r.content)
        return request.host_url + folderName + '/' + file
