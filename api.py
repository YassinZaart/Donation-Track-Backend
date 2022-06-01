from flask_restful import Resource, request, marshal_with, abort
from marshmallow import ValidationError

from variables import api, db
import db_operations, schemas, states, resource_fields


class User(Resource):
    @marshal_with(resource_fields.user_resource_fields)
    def get(self):
        args = request.args
        try:
            schemas.UserEmailSchema().load(args)
        except ValidationError as err:
            abort(message=err.messages, http_status_code=409)
        user = db_operations.get_user(args["email"])
        if user is None:
            abort(message="User not found", http_status_code=404)
        return user


class SignUp(Resource):

    def post(self):
        args = request.args
        try:
            schemas.SignUpInfoSchema().load(args)
        except ValidationError as err:
            abort(message=err.messages, http_status_code=400)
        state = db_operations.signup(args["email"], args["user_name"],
                                     args["password"])
        if state == states.SignupState.EMAIL_ALREADY_EXIST:
            message = {'message': 'User already exist'}
            return message, 409


class Login(Resource):
    def post(self):
        args = request.args
        try:
            schemas.LoginSchema().load(args)
        except ValidationError as err:
            abort(message=err.messages, http_status_code=400)

        state = db_operations.login(args["email"], args["password"])
        if state == states.LoginState.INCORRECT_PASSWORD:
            message = {'message': 'Incorrect password'}
            return message, 409
        if state == states.LoginState.USER_NOT_FOUND:
            message = {'message': 'User does not exist'}
            return message, 404
        message = {'message': 'Success!'}
        return message, 200


class Donation(Resource):
    def post(self):
        args = request.args
        try:
            schemas.DonationSchema().load(args)
        except ValidationError as err:
            abort(message=err.messages, http_status_code=400)
        state = db_operations.insert_donation(args["id"], args["user_name"], args["name"],
                                              args["description"],
                                              args["value"])
        if state == states.DonationInsertionState.USER_DOESNT_EXIST:
            message = {'message': 'Invalid User'}
            return message, 404
        if state == states.DonationInsertionState.DONEE_DOESNT_EXIST:
            message = {'message': 'Invalid Donee'}
            return message, 404
        message = {'message': 'Success!'}
        return message, 200

    def patch(self):
        args = request.args
        try:
            schemas.DonationUpdateSchema().load(args)
        except ValidationError as err:
            abort(message=err.messages, http_status_code=400)
        state = db_operations.update_donation(args["donation_id"], args["id"], args["user_name"], args["name"],
                                              args["description"],
                                              args["value"])
        if state == states.PostState.DOESNT_EXIST:
            abort(message="Donation does not exist", http_status_code=404)
        message = {'message': 'Success!'}
        return message, 200

    def delete(self):
        args = request.args
        try:
            schemas.DonationDeleteSchema().load(args)
        except ValidationError as err:
            abort(message=err.messages, http_status_code=400)
        state = db_operations.delete_donation(args["donation_id"]);
        if state == states.PostState.DOESNT_EXIST:
            abort(message="Donation does not exist", http_status_code=404)
        message = {'message': 'Success!'}
        return message, 200

    @marshal_with(resource_fields.donation_resource_fields)
    def get(self):
        args = request.args

        if "user_name" in args:
            donations = db_operations.get_donations_by_username(args["user_name"])
            if not donations:
                abort(message="Donation not found", http_status_code=404)
            return donations

        else:
            donations = db_operations.get_donations()
            if not donations:
                abort(message="Donation not found", http_status_code=404)
            return donations


class Post(Resource):
    def post(self):
        args = request.args
        try:
            schemas.PostSchema().load(args)
        except ValidationError as err:
            abort(message=err.messages, http_status_code=400)
        db_operations.insert_post(args["charity_name"], args["name"],
                                  args["address"], args["phone_number"],
                                  args["description"], args["value"])
        message = {'message': 'Success!'}
        return message, 200

    def patch(self):
        args = request.args
        try:
            schemas.PostUpdateSchema().load(args)
        except ValidationError as err:
            abort(message=err.messages, http_status_code=400)
        state = db_operations.update_post(args["post_id"], args["charity_name"], args["name"],
                                          args["address"], args["phone_number"],
                                          args["description"], args["value"])
        if state == states.PostState.DOESNT_EXIST:
            abort(message="Post does not exist", http_status_code=404)
        message = {'message': 'Success!'}
        return message, 200

    def delete(self):
        args = request.args
        try:
            schemas.PostDeleteSchema().load(args)
        except ValidationError as err:
            abort(message=err.messages, http_status_code=400)
        state = db_operations.delete_post(args["post_id"]);
        if state == states.PostState.DOESNT_EXIST:
            abort(message="Post does not exist", http_status_code=404)
        message = {'message': 'Success!'}
        return message, 200


    @marshal_with(resource_fields.post_resource_fields)
    def get(self):
        args = request.args
        if "charity_name" in args:
            try:
                schemas.PostCharityNameSchema().load(args)
            except ValidationError as err:
                abort(message=err.messages, http_status_code=400)
            posts = db_operations.get_posts_by_username(args["charity_name"])
            return posts
        else:
            posts = db_operations.get_posts()
            if posts is None:
                abort(message="No Posts", http_status_code=404)
            return posts


api.add_resource(User, "/users")
api.add_resource(Login, "/login")
api.add_resource(Donation, "/donations")
api.add_resource(SignUp, "/signup")
api.add_resource(Post, "/posts")
