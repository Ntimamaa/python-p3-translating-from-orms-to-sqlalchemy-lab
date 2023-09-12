from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Dog
from models import Base


engine = create_engine('sqlite:///mydatabase.db', echo=True)
Session = sessionmaker(bind=engine)

def create_table(engine, Base):
    Base.metadata.create_all(engine)

def save(session, dog_instance):
    session.add(dog_instance)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog_instance, new_breed):
    dog_instance.breed = new_breed
    session.commit()
    
if __name__ == "__main__":
    create_table(engine, Base)
