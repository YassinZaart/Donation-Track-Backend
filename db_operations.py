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


def signup(email: str, name: str, password: str) -> states.SignupState:
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


def get_donations_by_username(user_name: str) -> List[models.DonationModel]:
    donations = models.DonationModel.query.filter_by(user_name=user_name).order_by(
        desc(models.DonationModel.date)).all()
    return donations


def get_donations() -> List[models.DonationModel]:
    donations = models.DonationModel.query.order_by(desc(models.DonationModel.date)).all()
    return donations


def get_donation_by_id(id: str) -> models.DonationModel:
    donation = models.DonationModel.query.get(id)
    return donation


def get_donations_by_donee_id(id) -> List[models.DonationModel]:
    donations = models.DonationModel.query.filter_by(donee_id=id).order_by(desc(models.DonationModel.date)).all()
    return donations


def insert_donation(donee_id: str, user_name: str, name: str, description: str,
                    value: str) -> states.DonationInsertionState:
    donation = models.DonationModel(donee_id=donee_id, user_name=user_name, name=name, date=func.now(),
                                    description=description, value=value)
    db.session.add(donation)
    db.session.commit()
    return states.DonationInsertionState.INSERTION_SUCCESSFUL


def update_donation(donation_id: str, donee_id: str, user_name: str, name: str, description: str,
                    value: int):
    donation = models.DonationModel.query.filter_by(donation_id=donation_id).first()
    if not donation:
        return states.PostState.DOESNT_EXIST
    else:
        donation.donee_id = donee_id
        donation.user_name = user_name
        donation.name = name
        donation.description = description
        donation.value = value
    db.session.commit()
    return states.PostState.SUCCESSFUL


def delete_donation(donation_id):
    donation = models.DonationModel.query.filter_by(donation_id=donation_id).first()
    if not donation:
        return states.PostState.DOESNT_EXIST
    else:
        db.session.delete(donation)
        db.session.commit()
    return states.PostState.SUCCESSFUL


def insert_post(charity_name: str, name: str, location: str, phone_number: str, description: str, value: int):
    post = models.PostModel(charity_name=charity_name, name=name,
                            address=location, phone_number=phone_number, description=description, value=value)
    db.session.add(post)
    db.session.commit()


def update_post(post_id, charity_name: str, name: str, location: str, phone_number: str, description: str, value: int):
    post = models.PostModel.query.filter_by(id=post_id).first()
    if not post:
        return states.PostState.DOESNT_EXIST
    else:
        post.charity_name = charity_name
        post.name = name
        post.address = location
        post.phone_number = phone_number
        post.description = description
        post.value = value
    db.session.commit()
    return states.PostState.SUCCESSFUL


def delete_post(post_id):
    post = models.PostModel.query.filter_by(id=post_id).first()
    if not post:
        return states.PostState.DOESNT_EXIST
    else:
        db.session.delete(post)
        db.session.commit()
    return states.PostState.SUCCESSFUL


def get_posts():
    posts = models.PostModel.query.order_by(desc(models.PostModel.time_created)).all()
    return posts


def get_post_by_id(id: str):
    posts = models.PostModel.query.get(id)
    return posts


def get_posts_by_username(username: str):
    posts = models.PostModel.query.filter_by(charity_name=username).order_by(desc(models.PostModel.time_created)).all()
    return posts


def put_contribution(username: str, post_id: str, value: int):
    contribution = models.PostContributionModel.query.get((username, post_id))
    if contribution is None:
        contribution = models.PostContributionModel(username=username, post_id=post_id, value=value)
        db.session.add(contribution)
        db.session.commit()
    else:
        contribution.value = value
        db.session.commit()
    post = models.PostModel.query.get(post_id)
    sum = get_contributions_sum(post_id)
    post.contributions = sum
    db.session.commit()


def get_contributions(post_id: str):
    contributions = models.PostContributionModel.query.filter_by(post_id=post_id).all()
    return contributions


def get_contributions_sum(post_id: str):
    contributions = db.session.query(func.sum(models.PostContributionModel.value)) \
        .filter_by(post_id=post_id)
    sum = contributions.scalar()
    return sum


def get_requests():
    requests = models.RequestModel.query.order_by(desc(models.RequestModel.date)).all()
    return requests


def put_request(email: str, name: str, phone_number: str, address: str, type2: str, description: str):
    request = models.RequestModel.query.filter_by(email=email).first()
    if request is None:
        request = models.RequestModel(email=email, name=name, type=type2, phone_number=phone_number, address=address,
                                      description=description)
        db.session.add(request)
        db.session.commit()
    else:
        request.name = name
        request.phone_number = phone_number
        request.address = address
        request.description = description
        request.type = type2
        db.session.commit()


def accept_request(request_id):
    request = models.RequestModel.query.get(request_id)
    user = models.UserModel.query.get(request.email)
    user.phone_number = request.phone_number
    user.address = request.address
    user.description = request.description
    user.is_verified = True
    db.session.delete(request)
    db.session.commit()


def reject_request(request_id):
    request = models.RequestModel.query.get(request_id)
    db.session.delete(request)
    db.session.commit()
