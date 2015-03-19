#!flask/bin/python
from migrate.versioning import api
from config import ConfigClass

v = api.db_version(ConfigClass.SQLALCHEMY_DATABASE_URI, ConfigClass.SQLALCHEMY_MIGRATE_REPO)
api.downgrade(ConfigClass.SQLALCHEMY_DATABASE_URI, ConfigClass.SQLALCHEMY_MIGRATE_REPO, v - 1)
v = api.db_version(ConfigClass.SQLALCHEMY_DATABASE_URI, ConfigClass.SQLALCHEMY_MIGRATE_REPO)
print('Current database version: ' + str(v))