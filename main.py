from flask import Flask, render_template, request, jsonify
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import db

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://<user>:<passwd>@<ip>:<port>/<databasename>
db.init_app(app)
Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

@app.route("/")
def main():
    return jsonify({"msg": "ok"}),200

if __name__ == "__main__":
    manager.run()