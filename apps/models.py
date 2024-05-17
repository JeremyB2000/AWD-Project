from apps import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# Account Dimension Table
class AccountDimension(db.Model, UserMixin):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    comment = db.relationship('CommentDimension', backref='user')

    def set_password(self, unhashed_password):
        self.password = generate_password_hash(unhashed_password)

    def check_password(self, unhashed_password):
        return check_password_hash(self.password, unhashed_password)
    
# @login.user_loader
# def load_user(id):
#     return db.session.get(AccountDimension, int(id))

# Recipe Dimension Table
class RecipeDimension(db.Model):
    __tablename__ = 'recipe'
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    category = db.Column(db.String(100))
    status = db.Column(db.String(100))
    ingredients = db.Column(db.String(100))
    user = db.relationship('AccountDimension', backref='recipes')

# Comment Dimension Table
class CommentDimension(db.Model):
    __tablename__ = 'comment'
    comment_id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    comment = db.Column(db.Text)
    account = db.relationship('AccountDimension', backref='user_comments')
    recipe = db.relationship('RecipeDimension', backref='comments')