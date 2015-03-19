from migrate.versioning import api
from config import ConfigClass

api.upgrade(ConfigClass.SQLALCHEMY_DATABASE_URI, ConfigClass.SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(ConfigClass.SQLALCHEMY_DATABASE_URI, ConfigClass.SQLALCHEMY_MIGRATE_REPO)
print('Current database version: ' + str(v))