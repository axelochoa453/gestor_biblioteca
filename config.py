from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URI = "mysql+mysqlconnector://axel:blackzone4+@localhost/Biblioteca" #"mysql+mysqlconnector://usuario:contraseña@localost/Biblioteca"
engine = create_engine(DATABASE_URI, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

session = Session()
