# 初始化数据库连接:
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask_demo.db2 import Student

engine = create_engine('mysql+pymysql://abel:abel@192.168.10.194:3333/flask?charset=utf8')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
# classes1 = Classes(name='Python全栈')
# classes2 = Classes(name='Python全栈二期')
# classes3 = Classes(name='Python全栈三期')

# 添加到session:
# 单条增加
# session.add(classes1)
# 多条增加
# session.add_all([classes2, classes3])

# 查询
# 查询全部列
# res = session.query(Classes).all()
# for r in res:
#     print(r.id, r.name)

# 连表查询 手动查询
# res = session.query(Student.id, Student.username, Student.class_id, Classes.name).join(Classes, isouter=True).all()
# print(res)

# 连表 通过model里添加relationship来获得能力
res = session.query(Student).all()
for r in res:
    print(r.username, r.belong_classes.name)

# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
