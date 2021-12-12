from marshmallow import Schema, fields


class UserEmailSchema(Schema):
    email = fields.Str(required=True, error_messages={"required": "Email is required"})


class LoginSchema(UserEmailSchema):
    password = fields.Str(required=True, error_messages={"required": "Password is required"})


class UserNameSchema(Schema):
    name = fields.Str(required=True, error_messages={"required": "Name is required"})


class UserInfoSchema(UserEmailSchema):
    phone_number = fields.Str(required=True, error_messages={"required": "Phone number is required"})
    city = fields.Str(required=True, error_messages={"required": "City is required"})
    street = fields.Str(required=True, error_messages={"required": "Street is required"})
    name = fields.Str(required=True, error_messages={"required": "Name is required"})


class SignUpInfoSchema(UserInfoSchema):
    password = fields.Str(required=True, error_messages={"required": "Password is required"})


class DoneeIDSchema(Schema):
    id = fields.Int(required=True, error_messages={"required": "ID is required"})


class DoneeSchema(DoneeIDSchema):
    phone_number = fields.Str(required=True, error_messages={"required": "Phone number is required"})
    city = fields.Str(required=True, error_messages={"required": "City is required"})
    street = fields.Str(required=True, error_messages={"required": "Street is required"})
    first_name = fields.Str(required=True, error_messages={"required": "First Name is required"})
    last_name = fields.Str(required=True, error_messages={"required": "Last Name is required"})


class DonationSchema(Schema):
    donee_id = fields.Int(required=True, error_messages={"required": "ID is required"})
    user_name = fields.Str(required=True, error_messages={"required": "User name is required"})
    type = fields.Str(required=True, error_messages={"required": "Type is required"})
    value = fields.Int(required=True, error_messages={"required": "Value is required"})


class PostCharityNameSchema(Schema):
    charity_name = fields.Str(required=True, error_messages={"required": "Charity name is required"})


class PostSchema(PostCharityNameSchema):
    name = fields.Str(required=True, error_messages={"required": "Name is required"})
    address = fields.Str(required=True, error_messages={"required": "Address is required"})
    phone_number = fields.Str(required=True, error_messages={"required": "Phone number is required"})
    description = fields.Str(required=True, error_messages={"required": "Description is required"})
