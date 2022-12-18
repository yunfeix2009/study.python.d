# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand
from final_flask import db
from final_flask import app

manager = Manager(app)

Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    print(app.url_map)
    manager.run()
