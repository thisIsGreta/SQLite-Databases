###SQLite Databases### By Dr.Angela Yu, from Lecture 531-533 of 100 Days of Code

###SQLAlchemy###
#Definition: SQLAlchemy is defined as an ORM Object Relational Mapping library. 
#            This means that it's able to map the relationships in the database into Objects. 
#            Fields become Object properties. 
#            Tables can be defined as separate Classes and each row of data is a new Object.

# 1. Comment out all the existing code where we create an SQLite database directly using the sqlite3 module.
# 2. Install the required packages flask and flask_sqlalchemy and import the Flask and SQLAlchemy classes from each.
    pip install -U Flask-SQLAlchemy
    ```
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    ```
# 3. https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/ 
#    Create an SQLite database called new-books-collection.db
    ```
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    ```
# 4. Create a table in this database called books. The books table should contain 4 fields: id, title, author and rating. 
#    The fields should have the same limitations as before e.g. INTEGER/FLOAT/VARCHAR/UNIQUE/NOT NULL etc.
    ```
    class Books(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(80), unique=True, nullable=False)
        rating = db.Column(db.FLOAT, unique=True, nullable=False)

        def __repr__(self):
            return '<User %r>' % self.title
    db.create_all()
    ```
# 5. Create a new entry in the books table that consists of the following data.
    ```
    book = Books(id='1', title='Harry Potter', rating=7.5)
    db.session.add(book)
    db.session.commit()
    ```

### CRUD Operations with SQLAlchemy - Create, Read, Update, Delete ###
# 1. Create A New Record
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
# NOTE: When creating new records, the primary key fields is optional. you can also write: and the id field will be auto-generated.
    new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)

#2.1 Read All Records
    all_books = session.query(Book).all()
  
#2.2 Read A Particular Record by Query
    book = Book.query.filter_by(title="Harry Potter").first()
  
#3.1 Update A Particular Record By Query
    book_to_update = Book.query.filter_by(title="Harry Potter").first()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit() 
    
#3.2 Update A Record By PRIMARY KEY
    book_id = 1
    book_to_update = Book.query.get(book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()  

#4. Delete A Particular Record By PRIMARY KEY
    book_id = 1
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
#Note: You can also delete by querying for a particular value e.g. by title or one of the other properties.
