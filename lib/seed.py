#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()

### This code is for clearing out the database before a seeding. It will delete all data in the data base (not just the seeds)
# session.query(Game).delete()
# session.commit()


### Hard Code Seeding
# botw = Game(title="Breath of the Wild", platform="Switch", genre="Adventure", price=60)
# ffvii = Game(title="Final Fantasy VII", platform="Playstation", genre="RPG", price=30)
# mk8 = Game(title="Mario Kart 8", platform="Switch", genre="Racing", price=50)
# ccs = Game(title="Candy Crush Saga", platform="Mobile", genre="Puzzle", price=0)

# session.bulk_save_objects([botw, ffvii, mk8, ccs])
# session.commit()


### Dynamic Randomized Seeding
print("Seeding games...")

games = [
    Game(
        title=fake.name(),
        genre=fake.word(),
        platform=fake.word(),
        price=random.randint(0, 60)
    )
for i in range(50)]

session.bulk_save_objects(games)
session.commit()