import markdown
import os
import shelve

# Import the framework
from flask import Flask
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("categories.db")
    return db


@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        content = markdown_file.read()

        return markdown.markdown(content)


class CategoryList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        categories = []

        for key in keys:
            categories.append(shelf[key])

        return {'message': 'Success', 'data': categories}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('id', required=True)
        parser.add_argument('name', required=True)

        # Parse the arguments into an object
        args = parser.parse_args()
        shelf = get_db()
        shelf[args['id']] = args

        return {'message': 'Device registered', 'data': args}, 201


class Category(Resource):
    def get(self, id):
        shelf = get_db()

        # If the key oes not exists, return a 404 error.
        if not (id in shelf):
            return {'message': 'Device not found', 'data': {}}, 404

        return {'message': 'Device found', 'data': shelf[id]}, 200

    def delete(self, id):
        shelf = get_db()

        # If the key oes not exists, return a 404 error.
        if not (id in shelf):
            return {'message': 'Device not found', 'data': {}}, 404

        del shelf[id]
        return '', 204


api.add_resource(CategoryList, '/categories')
api.add_resource(Category, '/category/<string:id>')
