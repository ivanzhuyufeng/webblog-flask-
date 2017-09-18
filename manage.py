#!/usr/bin/python

import os
from app import create_app, db
from app.models import User, Role, Permission, Post
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


app = create_app(os.getenv('FLASK_CINFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app,db)

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Permission=Permission, Post=Post)

#@manager.command
#def deploy():
#    """Run deployment task."""
#    from flask_migrate import upgrade
#    from app.models import Role, User
#
#	#把数据库迁移到最新修订版本
#    upgrade()
#
#	#创建用户角色
#    Role.insert_roles()
#
#	#让所有用户关注此用户
#    User.add_self_follows()

manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
#    app.run()
