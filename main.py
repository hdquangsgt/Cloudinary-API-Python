from os.path import join, dirname, realpath
import base64
from routes.api import GenerateAPI
from flask import Flask, render_template_string

app = Flask(__name__, static_folder='upload')

if __name__ == "__main__":
    GenerateAPI(app).run()

    @app.route("/image/<string:fileName>")
    def display(fileName):
        fileImage = join(dirname(realpath(__file__)), 'upload/' + fileName)
        
        with open(fileImage, 'rb') as f:
            image = base64.b64encode(f.read()).decode('utf-8')
        return render_template_string('<img src="data:image/jpg;base64,{{image}}">', image=image)

    app.run(host='0.0.0.0', port=5000, debug=True)
