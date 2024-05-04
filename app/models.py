from typing import List, Optional
from app import db

# Comment Dimension Table
class CommentDimension(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    comment = db.Column(db.Text)

# Recipe Dimension Table
class RecipeDimension(db.Model):
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(100))
    status = db.Column(db.String(100))
    instructions = db.Column(db.Text, nullable=True)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment_dimension.comment_id'))

    def __repr__(self) -> str:
        return f'<RecipeDimension {self.recipe_id} {self.comment_id}>'

# Ingredient Dimension Table
class IngredientDimension(db.Model):
    ingredient_id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(255), nullable=False)

    def __repr__(self) -> str:
        return f'<IngredientDimension {self.ingredient_id} {self.ingredient_name}>'

# Combined Fact Table
class CombinedFactTable(db.Model):
    fact_id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe_dimension.recipe_id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient_dimension.ingredient_id'))

# Account Dimension Table
class AccountDimension(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

# Account Request Dimension Table
class AcctReqDimension(db.Model):
    act_req_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    recipe_id = db.Column(db.Integer)
