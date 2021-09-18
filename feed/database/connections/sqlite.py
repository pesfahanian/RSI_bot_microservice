import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import database_exists, create_database

logger = logging.getLogger(__name__)

Base = declarative_base()


class SQLite:
    def __init__(self) -> None:
        try:
            logger.info('Initializing SQLite database...')
            database_url = 'sqlite:///db.sqlite3'
            self.engine = create_engine(database_url)
            Base.metadata.create_all(self.engine)
            if not database_exists(self.engine.url):
                create_database(self.engine.url)
            Session = sessionmaker(bind=self.engine)
            self.session = scoped_session(Session)
            logger.info('SQLite database initialized!')
        except Exception as e:
            raise Exception('Failure in initializing the SQLite database. '
                            f'Reason: {str(e)}.')
