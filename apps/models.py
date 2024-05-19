from apps import db

# Account Dimension Table
class AccountDimension(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    comments = db.relationship('CommentDimension', back_populates='user')
    recipes = db.relationship('RecipeDimension', back_populates='recipe_user')

# Recipe Dimension Table
class RecipeDimension(db.Model):
    __tablename__ = 'recipe'
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    category = db.Column(db.String(100))
    status = db.Column(db.String(100))
    ingredients = db.Column(db.String(100))
    recipe_user = db.relationship('AccountDimension', back_populates='recipes')
    comments = db.relationship('CommentDimension', back_populates='recipe')

# Comment Dimension Table
class CommentDimension(db.Model):
    __tablename__ = 'comment'
    comment_id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    comment = db.Column(db.Text)
    user = db.relationship('AccountDimension', back_populates='comments')
    recipe = db.relationship('RecipeDimension', back_populates='comments')
