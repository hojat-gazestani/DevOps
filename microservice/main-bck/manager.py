from main import app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
#from flask.cli import FlaskGroup


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

#cli = FlaskGroup(app)

if __name__ == '__main__':
    manager.run()
    #cli()
