import ormar
import databases
import sqlalchemy

DATABASE_URL = f"sqlite:///dev.db"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    database = database
    metadata = metadata


def config_database(database_url=DATABASE_URL):
    engine = sqlalchemy.create_engine(database_url)
    BaseMeta.metadata.drop_all(engine)
    BaseMeta.metadata.create_all(engine)
