from flask_restful import fields

user_resource_fields = {
    'email': fields.String,
    'name': fields.String,
    'phone_number': fields.String,
    'address': fields.String,
    'description': fields.String,
    'is_verified': fields.Boolean,
    'is_admin': fields.Boolean
}

donation_resource_fields = {
    'donation_id': fields.Integer,
    'donee_id': fields.String,
    'user_name': fields.String,
    'name': fields.String,
    'date': fields.DateTime,
    'description': fields.String,
    'value': fields.Integer
}

post_resource_fields = {
    'id': fields.Integer,
    'charity_name': fields.String,
    'name': fields.String,
    'address': fields.String,
    'phone_number': fields.String,
    'description': fields.String,
    'time_created': fields.DateTime,
    'value': fields.Integer
}

post_contributions_resource_fields = {
    'username': fields.String,
    'post_id': fields.Integer,
    'value': fields.Integer
}


