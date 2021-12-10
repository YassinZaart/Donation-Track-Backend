from flask_restful import Resource, request, marshal_with, abort
from marshmallow import ValidationError

from donation_track_backend.variables import api
from donation_track_backend import db_operations, schemas, states, resource_fields


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
            abort(message=err.messages, http_status_code=409)
        state = db_operations.signup(args["email"], args["name"],
                                     args["password"], args["city"],
                                     args["street"], args["phone_number"])
        if state == states.SignupState.EMAIL_ALREADY_EXIST:
            message = {'message': 'User already exist'}
            return message, 409

        return 200


class Login(Resource):
    def post(self):
        args = request.args
        try:
            schemas.LoginSchema().load(args)
        except ValidationError as err:
            abort(message=err.messages, http_status_code=409)

        state = db_operations.login(args["email"], args["password"])
        if state == states.LoginState.INCORRECT_PASSWORD:
            message = {'message': 'Incorrect password'}
            return message, 409
        if state == states.LoginState.USER_NOT_FOUND:
            message = {'message': 'User does not exist'}
            return message, 404
        return 200


class Donee(Resource):
    def post(self):
        args = request.args
        try:
            schemas.DoneeSchema().load(args)
        except ValidationError as err:
            return err.messages, 409
        state = db_operations.insert_donee(args["id"], args["first_name"], args["last_name"],
                                           args["city"], args["street"], args["phone_number"])
        if state == states.DoneeInsertionState.DONEE_EXISTS:
            message = {'message': 'Donee already exist'}
            return message, 409
        return 200

    @marshal_with(resource_fields.donee_resource_fields)
    def get(self):
        args = request.args
        try:
            schemas.DoneeIDSchema().load(args)
        except ValidationError as err:
            abort(message=err.messages, http_status_code=409)
        donee = db_operations.get_donee(args["id"])
        if donee is None:
            abort(message="Invalid ID", http_status_code=404)
        return donee


class Donation(Resource):
    def post(self):
        args = request.args
        try:
            schemas.DonationSchema().load(args)
        except ValidationError as err:
            abort(message=err.messages, http_status_code=409)
        state = db_operations.insert_donation(args["donee_id"], args["user_name"],
                                              args["date"], args["type"],
                                              args["value"])
        if state == states.DonationInsertionState.USER_DOESNT_EXIST:
            message = {'message': 'Invalid User'}
            return message, 404
        if state == states.DonationInsertionState.DONEE_DOESNT_EXIST:
            message = {'message': 'Invalid Donee'}
            return message, 404
        return 200

    @marshal_with(resource_fields.donation_resource_fields)
    def get(self):
        args = request.args
        if "donee_id" in args:
            donations = db_operations.get_donations_by_donee(args["donee_id"])
            if donations is None:
                abort(message="Donation not found", http_status_code=409)
            return donations

        if "user_name" in args:
            donations = db_operations.get_donations_by_user(args["user_name"])
            if donations is None:
                abort(message="Donation not found", http_status_code=409)
            return donations
        if "user_name" in args & "donee_id" in args:
            abort(message="donee_id and user_name can't be in the same request", http_status_code=409)
        abort(message="donee_id or user_name arguments are missing", http_status_code=400)


api.add_resource(User, "/users")
api.add_resource(Login, "/login")
api.add_resource(Donee, "/donees")
api.add_resource(Donation, "/donations")
api.add_resource(SignUp, "/signup")
