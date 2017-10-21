# coding: utf-8

import sys
import os
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from app import db, app
from app.models import Suan

# 编码设置
reload(sys)
sys.setdefaultencoding('utf-8')

manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    """自动加载环境"""
    return dict(
        app = app,
        db = db,
        Suan = Suan
    )

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

