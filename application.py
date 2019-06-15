import os
DEBUG=True

# sqlalchemy URI takes postgresql:///dbname for a trusted connection (localhost with no pwd)
# else it shold be postgresql://user:password@servername:port/dbname
# Every server has a default db called postgres which could be used to connect to
# and then a new db with desired name could be created!
# export DATABASE_URL = "postgresql:///mynoteapp1"
# SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL']
SQLALCHEMY_DATABASE_URI='postgresql://postgres:harshita@localhost:5432/mynoteapp1'
