from marshmallow import Schema, fields


class UserEmailSchema(Schema):
    email = fields.Str(required=True, error_messages={"required": "Email is required"})


class LoginSchema(UserEmailSchema):
    password = fields.Str(required=True, error_messages={"required": "Password is required"})


class UserNameSchema(Schema):
    name = fields.Str(required=True, error_messages={"required": "Name is required"})


class UserInfoSchema(UserEmailSchema):
    phone_number = fields.Str(required=True, error_messages={"required": "Phone number is required"})
    address = fields.Str(required=True, error_messages={"required": "Address is required"})
    name = fields.Str(required=True, error_messages={"required": "Name is required"})


class SignUpInfoSchema(Schema):
    user_name = fields.Str(required=True, error_messages={"required": "user_name is required"})
    email = fields.Str(required=True, error_messages={"required": "email is required"})
    password = fields.Str(required=True, error_messages={"required": "Password is required"})


class DonationSchema(Schema):
    user_name = fields.Str(required=True, error_messages={"required": "User name is required"})
    name = fields.Str(required=True, error_messages={"required": "name is required"})
    id = fields.Str(required=True, error_messages={"required": "ID is required"})
    description = fields.Str(description=True, error_messages={"required": "Description is required"})
    value = fields.Int(required=True, error_messages={"required": "Value is required"})


class DonationUpdateSchema(DonationSchema):
    donation_id = fields.Str(required=True, error_messages={"required": "Donation ID is required"})


class DonationDeleteSchema(Schema):
    donation_id = fields.Str(required=True, error_messages={"required": "Donation ID is required"})


class PostCharityNameSchema(Schema):
    charity_name = fields.Str(required=True, error_messages={"required": "Charity name is required"})


class PostSchema(PostCharityNameSchema):
    name = fields.Str(required=True, error_messages={"required": "Name is required"})
    address = fields.Str(required=True, error_messages={"required": "Address is required"})
    phone_number = fields.Str(required=True, error_messages={"required": "Phone number is required"})
    description = fields.Str(required=True, error_messages={"required": "Description is required"})
    value = fields.Int(required=True, error_messages={"required": "Value is required"})


class PostUpdateSchema(PostSchema):
    post_id = fields.Integer(required=True, error_messages={"required": "Post ID is required"})


class PostIDSchema(Schema):
    post_id = fields.Integer(required=True, error_messages={"required": "Post ID is required"})


class PostContribution(Schema):
    post_id = fields.Integer(required=True, error_messages={"required": "Post ID is required"})
    user_name = fields.String(required=True, error_messages={"required": "Username is required"})
    value = fields.Integer(required=True, error_messages={"required": "Value ID is required"})
