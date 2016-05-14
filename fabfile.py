from fabric.api import *

def create_database():
    """Creates role and database"""
    db_user = 'fit'
    db_pass = 'password'
    db_table = 'fit_content'
    sudo('psql -c "CREATE USER %s WITH PASSWORD \'%s\'"' % (db_user, db_pass), user='postgres')
    sudo('psql -c "CREATE DATABASE %s WITH OWNER %s"' % (
        db_table, db_user), user='postgres')
    # allow db_user create test db when running python manage.py test polls
    sudo('psql -c "ALTER USER %s CREATEDB"' % db_user, user='postgres')