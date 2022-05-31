from typing import Optional, List

from sqlalchemy import desc, func

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


def signup(email: str, name: str, password: str, address: str, phone_number: str,
           description: str) -> states.SignupState:
    user = models.UserModel.query.get(email)
    pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    if user is not None:
        return states.SignupState.EMAIL_ALREADY_EXIST
    user = models.UserModel(email=email, name=name, password=pw_hash)
    db.session.add(user)
    db.session.commit()
    return states.SignupState.SIGNUP_SUCCESSFUL


def get_user(email: str) -> Optional[models.UserModel]:
    user = models.UserModel.query.get(email)
    return user


def get_donations(user_name: str) -> List[models.DonationModel]:
    donations = models.DonationModel.query.filter_by(user_name=user_name).order_by(desc(models.DonationModel.date)).all()
    return donations


def get_donations() -> List[models.DonationModel]:
    donations = models.DonationModel.query.order_by(desc(models.DonationModel.date)).all()
    return donations


def insert_donation(donee_id: str, user_name: str, name: str, description: str,
                    value: str) -> states.DonationInsertionState:
    donation = models.UserModel.query.filter_by(name=user_name).first()
    if donation is None:
        return states.DonationInsertionState.USER_DOESNT_EXIST
    donation = models.DonationModel(donee_id=donee_id, user_name=user_name, name=name, date=func.now(),
                                    description=description, value=value)
    db.session.add(donation)
    db.session.commit()
    return states.DonationInsertionState.INSERTION_SUCCESSFUL


def insert_post(charity_name: str, name: str, location: str, phone_number: str, description: str, value: int):
    post = models.PostModel(charity_name=charity_name, user_name=name,
                            address=location, phone_number=phone_number, description=description, value=value)
    db.session.add(post)
    db.session.commit()


def get_posts():
    posts = models.PostModel.query.order_by(desc(models.PostModel.time_created)).all()
    return posts


def get_posts(email: str):
    posts = models.PostModel.query.filter_by(email=email).order_by(desc(models.PostModel.time_created)).all()
    return posts


def put_contribution(email: str, post_id: str, value: int):
    contribution = models.PostContributionModel.query.get((email, post_id))
    if contribution is None:
        contribution = models.PostContributionModel(email=email, post_id=post_id, value=value)
        db.session.add(contribution)
        db.session.commit()
    else:
        contribution.value = value
        db.session.commit()
