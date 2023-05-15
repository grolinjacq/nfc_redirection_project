# config.py

import os

# Get the absolute path to the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

class Config:
    # SQLite database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(current_dir, 'nfc_data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Other configuration options for your Flask application
    # ...

# Create an instance of the Config class
config = Config()
