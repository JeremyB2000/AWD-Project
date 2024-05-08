#import tables_delete

from app import db

tables = db.metadata.tables

for table in tables.values():
    db.session.execute(table.delete())

db.session.commit()
