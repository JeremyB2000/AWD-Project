from apps import db


# Account Dimension Table
class AccountDimension(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)


class RecipeDimension(db.Model):
    __tablename__ = 'recipe'
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    category = db.Column(db.String(100))
    status = db.Column(db.String(100))
    ingredients = db.Column(db.String(100))
    user = db.relationship('AccountDimension', backref='account')

# Comment Dimension Table
