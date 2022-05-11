from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

sfcstudents = {}

sfcstudentpostdata = reqparse.RequestParser()
sfcstudentpostdata.add_argument(
    "gakubu", type=str, help="生徒の所属学部", required=True)
sfcstudentpostdata.add_argument(
    "class", type=str, help="生徒の所属学部", required=True)


class Students(Resource):
    def get(self, studentname):
        return sfcstudents[studentname]

    def post(self, studentname):
        sfcstudents[studentname] = sfcstudentpostdata.parse_args()
        return sfcstudents[studentname], 201

    def put(self, studentname):
        sfcstudents[studentname] = sfcstudentpostdata.parse_args()
        return sfcstudents[studentname], 204

    def delete(self, studentname):
        del sfcstudents[studentname]
        return "Deleted data", 204


api.add_resource(Students, "/sfcstudents/<string:studentname>")

if __name__ == "__main__":
    app.run(debug=True)
