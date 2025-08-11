from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func
import uuid

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20), unique=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    registrations = relationship("Registration", back_populates="user")


class Course(Base):
    __tablename__ = 'courses'

    course_id = Column(Integer, primary_key=True)
    course_name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)

    registrations = relationship("Registration", back_populates="course")


class Registration(Base):
    __tablename__ = 'registrations'

    registration_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.course_id'), nullable=False)
    registration_date = Column(TIMESTAMP, server_default=func.now())
    payment_status = Column(Enum('pending', 'completed', 'failed'), default='pending')

    user = relationship("User", back_populates="registrations")
    course = relationship("Course", back_populates="registrations")


# Initialize database connection
engine = create_engine('mysql+mysqlconnector://user:password@localhost/your_database')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)