from app import db
from app.models import *

account1 = AccountDimension(email='user1@example.com', username='user1', password='password1')
account2 = AccountDimension(email='user2@example.com', username='user2', password='password2')
account3 = AccountDimension(email='user3@example.com', username='user3', password='password3')

recipe1 = RecipeDimension(recipe_name='Recipe 1', user_id=1, category='Dinner', status='Complete', ingredients='a, b, c, d')
recipe2 = RecipeDimension(recipe_name='Recipe 2', user_id=2, category='Lunch', status='Incomplete', ingredients='e, f, g, h')
recipe3 = RecipeDimension(recipe_name='Recipe 3', user_id=3, category='Breakfast', status='Complete', ingredients='i, j, k, l')

comment1 = CommentDimension(recipe_id=1, user_id=1, comment='Comment 1 for recipe 1')
comment2 = CommentDimension(recipe_id=2, user_id=2, comment='Comment 2 for recipe 2')
comment3 = CommentDimension(recipe_id=3, user_id=3, comment='Comment 3 for recipe 3')

test_data = [
    account1, account2, account3,
    recipe1, recipe2, recipe3,
    comment1, comment2, comment3
]

for data in test_data:
    db.session.add(data)

db.session.commit()