from typing import Optional, List

from sqlalchemy import DateTime

from variables import db, bcrypt
import states, models


def login(email: str, password: str) -> states.LoginState:
    user = models.UserModel.query.get(email)
    if user is None:
        return states.LoginState.USER_NOT_FOUND
    if bcrypt.check_password_hash(user.password, password):
        return states.LoginState.LOGIN_SUCCESSFUL
    else:
        return states.LoginState.INCORRECT_PASSWORD


def signup(email: str, name: str, password: str, city: str, street: str, phone_number: str) -> states.SignupState:
    user = models.UserModel.query.get(email)
    pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    if user is not None:
        return states.SignupState.EMAIL_ALREADY_EXIST
    user = models.UserModel(email=email, name=name, phone_number=phone_number,
                            city=city, street=street, password=pw_hash, is_admin=False)
    db.session.add(user)
    db.session.commit()
    return states.SignupState.SIGNUP_SUCCESSFUL


def get_user(email: str) -> Optional[models.UserModel]:
    user = models.UserModel.query.get(email)
    return user


def get_donee(id: str) -> Optional[models.DoneeModel]:
    user = models.DoneeModel.query.get(id)
    return user


def insert_donee(id: str, fname: str, lname: str, city: str, street: str,
                 phone_number: str) -> states.DoneeInsertionState:
    donee = models.DoneeModel.query.get(id)
    if donee is not None:
        return states.DoneeInsertionState.DONEE_EXISTS
    donee = models.DoneeModel(id=id, first_name=fname, last_name=lname, city=city,
                              street=street, phone_number=phone_number)
    db.session.add(donee)
    db.session.commit()
    return states.DoneeInsertionState.INSERTION_SUCCESSFUL


def get_donations_by_donee(id: str) -> List[models.DonationModel]:
    donations = models.DonationModel.query.filter_by(id=id).all()
    return donations


def get_donations_by_user(name: str) -> List[models.DonationModel]:
    donations = models.DonationModel.query.filter_by(user_name=name).all()
    return donations


def get_donations_by_donee(id: str) -> List[models.DoneeModel]:
    donations = models.DonationModel.query.filter_by(donee_id=id).all()
    return donations


def insert_donation(donee_id: str, user_name: str, date_time: DateTime, type: str,
                    value: str) -> states.DonationInsertionState:
    donation = models.DonationModel.query.filter_by(donee_id=donee_id).first()
    if donation is None:
        return states.DonationInsertionState.DONEE_DOESNT_EXIST
    donation = models.DonationModel.query.filter_by(user_name=user_name).first()
    if donation is None:
        return states.DonationInsertionState.USER_DOESNT_EXIST
    donation = models.DonationModel(donee_id=donee_id, user_name=user_name, date=date_time,
                                    type=type, value=value)
    db.session.add(donation)
    db.session.commit()
    return states.DonationInsertionState.INSERTION_SUCCESSFUL


def insert_post(charity_name: str, name: str, location: str, phone_number: str, description: str):
    post = models.PostModel(charity_name, name, location, phone_number, description)
    db.session.add(post)
    db.session.commit()


def get_posts(charity_name: str):
    donations = models.PostModel.query.filter_by(charity_name=charity_name).all()
    return donations
