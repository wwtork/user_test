#!flask/bin/python
from migrate.versioning import api
from config import ConfigClass
from init_app import db
import os.path
db.create_all()
if not os.path.exists(ConfigClass.SQLALCHEMY_MIGRATE_REPO):
    api.create(ConfigClass.SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(ConfigClass.SQLALCHEMY_DATABASE_URI, ConfigClass.SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(ConfigClass.SQLALCHEMY_DATABASE_URI, ConfigClass.SQLALCHEMY_MIGRATE_REPO, api.version(ConfigClass.SQLALCHEMY_MIGRATE_REPO))