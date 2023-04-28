from flask_restful import Api
from controllers.handleController import HandleCloudinary

class GenerateAPI():
    def __init__(self, flask):
        self.api = Api(flask)
    
    def run(self):
        # Define url at here
        self.api.add_resource(HandleCloudinary, "/handle")
