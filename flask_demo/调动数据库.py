# 初始化数据库连接:
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask_demo.TestModel import User

engine = create_engine('mysql+pymysql://abel:abel@192.168.10.194:3333/flask?charset=utf8')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='5', name='Bob')
new_user2 = User(id='11', name='Tank')
# 添加到session:
session.add(new_user)
session.add(new_user2)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
