from flask import abort, Flask, request, jsonify
import json
from data import *

app = Flask(__name__)


@app.route("/all_work", methods=["GET"])
def list_work_experience():
   return {"juliana work experiences": get_all_work_experience()}


@app.route("/work/<id>", methods=["GET"])
def check_work_experience(id):
   return {"juliana work": get_work(int(id))}


@app.route("/set_work/<id>", methods=["POST"])
def set_new_work_experience(id):
   data = request.json
   if not data:
      abort(400, 'Missing new work')
   return {"Juliana work experience": create_new_work(int(id), data)}


@app.route("/all_education", methods=["GET"])
def list_education():
   return {"Juliana education": get_all_education()}


@app.route("/skills", methods=["GET"])
def list_skills():
   return {"Some skills": get_all_skils()}


@app.route("/academic_projects", methods=["GET"])
def list_projects():
   return {"Academic Projects": get_all_academic_projects()}


if __name__ == "__main__":
    app.run(debug=True)
