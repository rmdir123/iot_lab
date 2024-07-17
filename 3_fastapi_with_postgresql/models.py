from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

from database import Base

class Student(Base):
    __tablename__ = 'students'

    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    id = Column(Integer, primary_key=True, index=True)
    dob = Column(String, index=True)
    gender = Column(String, index=True)

