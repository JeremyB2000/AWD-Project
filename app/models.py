from typing import List, Optional
from app import db


class CommentDimension(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.column(db.Integer, db.ForeignKey('recipe_dimension.recipe_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('account_dimension.user_id'))
    comment = db.Column(db.Text)
    #Recipe ID: one recipe id - many comment id
    #User ID: one user id - one comment id

# Recipe Dimension Table
class RecipeDimension(db.Model):
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('account_dimension.user_id'))
    category = db.Column(db.String(100))
    status = db.Column(db.String(100))
    ingredients = db.Column(db.String(100))
    #User ID: one user id - many recipe id's
    user = db.relationship('AccountDimension', backref='account')

# Account Dimension Table
class AccountDimension(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))