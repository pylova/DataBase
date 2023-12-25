from db import Base, Session, engine
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime

s = Session()


class User(Base):
    __tablename__ = 'User'
    User_id = Column(Integer, primary_key=True)
    Phone_number = Column(String)
    Email = Column(String)
    First_name = Column(String)
    Last_name = Column(String)

    user_class = relationship("UserClasses")

    def __init__(self, user_id, phone_number, email, first_name, last_name):
        self.User_id = user_id
        self.Phone_number = phone_number
        self.Email = email
        self.First_name = first_name
        self.Last_name = last_name

    def __repr__(self):
        return f"<Users(User_id={self.User_id}, Phone_number={self.Phone_number}, Email={self.Email}, First_name={self.First_name}, Last_name={self.Last_name})>"


class Class(Base):
    __tablename__ = 'Classes'
    Classes_id = Column(Integer, primary_key=True)
    Title = Column(String)
    Date_and_Time = Column(DateTime)
    Duration = Column(Numeric)
    Location = Column(String)

    instructor = relationship("Instructor")
    user_class = relationship("UserClasses")

    def __init__(self, class_id, title, date_and_time, duration, location):
        self.Classes_id = class_id
        self.Title = title
        self.Date_and_Time = date_and_time
        self.Duration = duration
        self.Location = location

    def __repr__(self):
        return f"<Classes(Classes_id={self.Classes_id}, Title={self.Title}, Date_and_Time={self.Date_and_Time}, Duration={self.Duration}, Location={self.Location})>"


class Instructor(Base):
    __tablename__ = 'Instructor'
    Instructor_id = Column(Integer, primary_key=True)
    First_name = Column(String)
    Last_name = Column(String)

    Classes_id = Column(Integer, ForeignKey('Classes.Classes_id'))

    def __init__(self, instructor_id, first_name, last_name, class_id):
        self.Instructor_id = instructor_id
        self.First_name = first_name
        self.Last_name = last_name
        self.Classes_id = class_id

    def __repr__(self):
        return f"<Instructor(Instructor_id={self.Instructor_id}, First_name={self.First_name}, Last_name={self.Last_name}, Classes_id={self.Classes_id})>"


class UserClasses(Base):
    __tablename__ = 'User_Classes'

    User_id = Column(Integer, ForeignKey('User.User_id'), primary_key=True)
    Classes_id = Column(Integer, ForeignKey('Classes.Classes_id'), primary_key=True)

    def __init__(self, user_id, classes_id):
        self.User_id = user_id
        self.Classes_id = classes_id

    def __repr__(self):
        return f"<User_Classes(User_id={self.User_id}, Classes_id={self.Classes_id})>"


class Model:
    def __init__(self):
        self.session = Session()
        self.connection = engine.connect()

    def insert_user(self, user_id: int, phone_number: str, email: str, first_name: str, last_name: str) -> None:
        user = User(user_id=user_id, phone_number=phone_number, email=email, first_name=first_name, last_name=last_name)
        s.add(user)
        s.commit()

    def insert_class(self, class_id: int, title: str, date_and_time: DateTime, duration: int, location: str) -> None:
        clas = Class(class_id=class_id, title=title, date_and_time=date_and_time, duration=duration, location=location)
        s.add(clas)
        s.commit()

    def insert_instructor(self, instructor_id: int, first_name: str, last_name: str, class_id: int) -> None:
        instructor = Instructor(instructor_id=instructor_id, first_name=first_name, last_name=last_name, class_id=class_id)
        s.add(instructor)
        s.commit()

    def insert_user_class(self, user_id: int, classes_id: int) -> None:
        user_class = UserClasses(user_id=user_id, classes_id=classes_id)
        s.add(user_class)
        s.commit()

    @staticmethod
    def show_users():
        return s.query(User.User_id, User.Phone_number, User.Email, User.First_name, User.Last_name).all()

    @staticmethod
    def show_classes():
        return s.query(Class.Classes_id, Class.Title, Class.Date_and_Time, Class.Duration, Class.Location).all()

    @staticmethod
    def show_instructors():
        return s.query(Instructor.Instructor_id, Instructor.First_name, Instructor.Last_name, Instructor.Classes_id).all()

    @staticmethod
    def show_user_classes():
        return s.query(UserClasses.User_id, UserClasses.Classes_id).all()

    @staticmethod
    def update_user(user_id: int, phone_number: str, email: str, first_name: str, last_name: str, id: int) -> None:
        s.query(User).filter_by(User_id=id).update({User.User_id: user_id, User.Phone_number: phone_number, User.Email: email, User.First_name: first_name, User.Last_name: last_name})
        s.commit()

    @staticmethod
    def update_class(class_id: int, title: str, date_and_time: DateTime, duration: int, location: str, id: int) -> None:
        s.query(Class).filter_by(Classes_id=id).update({Class.Classes_id: class_id, Class.Title: title, Class.Date_and_Time: date_and_time, Class.Duration: duration, Class.Location: location})
        s.commit()

    @staticmethod
    def update_instructor(instructor_id: int, first_name: str, last_name: str, class_id: int, id: int) -> None:
        s.query(Instructor).filter_by(Instructor_id=id).update({Instructor.Instructor_id: instructor_id, Instructor.First_name: first_name, Instructor.Last_name: last_name, Instructor.Classes_id: class_id})
        s.commit()

    @staticmethod
    def update_user_class(user_id: int, class_id: int, id: int) -> None:
        s.query(UserClasses).filter_by(User_id=id).update({UserClasses.User_id: user_id, UserClasses.Classes_id: class_id})
        s.commit()

    @staticmethod
    def delete_user(user_id) -> None:
        user = s.query(User).filter_by(User_id=user_id).one()
        s.delete(user)
        s.commit()

    @staticmethod
    def delete_class(class_id) -> None:
        clas = s.query(Class).filter_by(Classes_id=class_id).one()
        s.delete(clas)
        s.commit()

    @staticmethod
    def delete_instructor(instructor_id) -> None:
        instructor = s.query(Instructor).filter_by(Instructor_id=instructor_id).one()
        s.delete(instructor)
        s.commit()

    @staticmethod
    def delete_user_class(user_id) -> None:
        user_classes = s.query(UserClasses).filter_by(User_id=user_id).all()
        for user_class in user_classes:
            s.delete(user_class)
        s.commit()