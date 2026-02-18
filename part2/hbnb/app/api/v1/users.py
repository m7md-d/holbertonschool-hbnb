from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('users', description='Users operations')

user_model = api.model('User', {
    'first_name': fields.String(required=True, description='first name of the user'),
    'last_name': fields.String(required=True, description='last name of the user'),
    'email': fields.String(required=True, description='Email address of the user')
})

@api.route('/')
class Users(Resource):
    @api.expect(user_model)
    @api.response(201, 'user sucessfuly register')
    @api.response(400, 'invalid input')
    def post(self):
        """register user"""
        user_data = api.payload

        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 409

        new_user = facade.create_user(user_data)
        if new_user:
            return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email}, 201
        else:
            return {'error': 'Invalid input data'}, 400
        
    
    @api.response(200, 'users is fetched')
    def get(self):
        """Retrieve a list of all users"""
        users = facade.get_all_users()
        return [{'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email} for user in users], 200
    