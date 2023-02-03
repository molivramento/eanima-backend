import ormar
import databases
import sqlalchemy
from decouple import config


if bool(config('DEV')):
    DATABASE_URL = config('file')
else:
    name = config('name')
    user = config('user')
    password = config('password')
    host = config('host')
    port = config('port')
    DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{name}"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    database = database
    metadata = metadata


def config_database(database_url=DATABASE_URL):
    engine = sqlalchemy.create_engine(database_url)
    # BaseMeta.metadata.drop_all(engine)
    BaseMeta.metadata.create_all(engine)
