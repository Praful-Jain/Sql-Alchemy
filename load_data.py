import csv
from sqlalchemy.orm import sessionmaker
from build_tables import Match, Delivery, Umpire,engine

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Load csv data into tables
def load_data(csv_path, model_class, sample_session):
    with open(csv_path, 'r',encoding='latin-1') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            data = {key.strip(): value for key, value in row.items()}
            sample_session.add(model_class(**data))
    sample_session.commit()


# CSV files location
matches_csv = '/home/praful/PROJECT/IPL dataset analytics/matches.csv'
umpires_csv = '/home/praful/PROJECT/IPL dataset analytics/umpires.csv'
deliveries_csv = '/home/praful/PROJECT/IPL dataset analytics/deliveries.csv'

# Calling load_data function
load_data(matches_csv, Match, session)
load_data(umpires_csv, Umpire, session)
load_data(deliveries_csv, Delivery, session)

# close session
session.close()


