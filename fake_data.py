
from faker import Faker
from faker.providers import BaseProvider
from faker.providers import internet
import random
import csv
from datetime import datetime
import pandas as pd


class GenereProvider(BaseProvider):
    def movie_genre(self):
        return random.choice(['Documentary', 'Thriller', 'Mystery', 'Horror', 'Action', 'Comedy', 'Drama', 'Romance'])

class LanguageProvider(BaseProvider):
    def language(self):
        return random.choice(['English', 'Chinese', 'Italian', 'Spanish', 'Hindi', 'Japanese'])

RECORD_COUNT = 200

fake = Faker()
fake.add_provider(internet)
fake.add_provider(GenereProvider)
fake.add_provider(LanguageProvider)

def capitalize(str):
    return str.capitalize()

def get_movie_name():
    words = fake.words()
    capitalized_words = list(map(capitalize, words))
    return ' '.join(capitalized_words)

def get_movie_date():
    return datetime.strftime(fake.date_time_this_decade(), "%B %d, %Y")

def get_movie_len():
    return random.randrange(50, 150)

def get_movie_rating():
    return round(random.uniform(1.0, 5.0), 1)

def generate_movie():
    return [fake.name(),fake.ssn(), fake.city(), fake.state_abbr() ,fake.postcode(), fake.phone_number(), fake.date_of_birth(),fake.email(), get_movie_name(), fake.movie_genre(), get_movie_date(), get_movie_len(), get_movie_rating(), fake.language()]
#    return [fake.name(),fake.ssn(), fake.city(), fake.state_abbr() ,fake.postcode()]


date = datetime.strftime(fake.date_time_this_decade(), "%B %d, %Y")
print(date) # April 30, 2020

#df = pd.DataFrame([])

with open('movie_data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'SSN', 'City', 'State', 'PostalCode', 'Phone', 'DOB', 'Email', 'Title', 'Genre', 'Premiere', 'Runtime', 'IMDB Score', 'Language'])
#    writer.writerow(['Name', 'SSN', 'City', 'State', 'PostalCode'])

    for i in range(RECORD_COUNT):
    #print(f'{name}, {address}, {phone}, {email}, {movie_name}, {movie_genre}, {movie_date}, {movie_len},  {movie_rating}, {movie_language}')
    #print(generate_movie())
        writer.writerow(generate_movie())


