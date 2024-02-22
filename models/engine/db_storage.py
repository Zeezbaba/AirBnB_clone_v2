#!/usr/bin/python3

from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """create the engine"""
        hbnb_dev = getenv('HBNB_MYSQL_USER')
        hbnb_dev_pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        hbnb_dev_db = getenv('HBNB_MYSQL_DB')
        db = "mysql+mysqldb://{}:{}@{}:3306/{}".format(
                hbnb_dev, hbnb_dev_pwd, host, hbnb_dev_db)
        self.__engine = create_engine(db, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):

        if cls:
            all_obj = self.__session.query(self.classes()[cls]).all()
        else:
            all_obj = self.__session.query(State).all()
            all_obj += self.__session.query(User).all()
            all_obj += self.__session.query(City).all()
            all_obj += self.__session.query(Amenity).all()
            all_obj += self.__session.query(Place).all()
            all_obj += self.__session.query(Review).all()

            dictionary = {}
            for obj in all_obj:
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                dictionary[key] = obj
            retuurn dictionary

    def new(self, obj):
        """add the object to the current database
        session
        """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current
        database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database.
        create the current database session (self.__session) from
        the engine (self.__engine) by using a sessionmaker
        """

        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        Base.metadata.create_all(self.__engine)

        Session = scoped_session(self.__session)
        self.__session = Session()

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"Basemodel": Basemodel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes
