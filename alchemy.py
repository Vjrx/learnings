from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_uri = 'sqlite:///test.db'
engine = create_engine(db_uri, echo=True)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    """Data model example."""
    __tablename__ = "user"

    username = Column(String(100), nullable=False, primary_key=True)
    password = Column(String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<Example model {}>'.format(self.username)


# Creating a new User and saving it
Base.metadata.create_all(engine)
user = User(username='vijay2', password='vijayanand')
session.add(user)
session.commit()

# Querying db
res = session.query(User).all()

for i in res:
    print(i.username)








