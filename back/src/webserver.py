from flask import Flask, request
from flask_cors import CORS
from src.domain.machines import Machine

from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/info", methods=["GET"])
    def info_get():
        info = repositories["info"].get_info()
        return object_to_json(info)
    
    @app.route("/api/process/register", methods=["POST"])
    def regist_machine():
        data = request.json
        washer_machine = Machine( 
           id_machine= data['id_machine'],
                brand= data['brand'],
                model= data['model'],
                register_date= data['register_date'],
                employee= data['employee']
        )
          
        repositories["machine"].save(washer_machine)
        return '', 200

    return app
