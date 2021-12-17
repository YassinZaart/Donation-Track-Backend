from flask_restful import fields

user_resource_fields = {
    'email': fields.String,
    'name': fields.String,
    'phone_number': fields.String,
    'city': fields.String,
    'street': fields.String,
    'is_admin': fields.Boolean
}

donee_resource_fields = {
    'id': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
    'city': fields.String,
    'street': fields.String,
    'phone_number': fields.String
}

donation_resource_fields = {
    'id': fields.String,
    'name': fields.String,
    'date': fields.DateTime,
    'type': fields.String,
    'value': fields.Integer
}

post_resource_fields = {
    'user_name': fields.String,
    'address': fields.String,
    'phoneNumber': fields.String,
    'description': fields.String,
    'time_created': fields.DateTime
}
