# 初始化数据库连接:
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from flask_demo.db2 import Classes

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
res = session.query(Classes).all()
for r in res:
    print(r.id, r.name)

# 查询指定列
# res = session.query(Classes.id, Classes.name).all()
# print(res)

# 查询 列改别名
# res = session.query(Classes.id, Classes.name.label('xx')).all()
# print([r.xx for r in res])

# res = session.query(Classes).filter(Classes.name == 'Python全栈二期099099099099').all()
# res = session.query(Classes).filter_by(name='Python全栈二期099099099099').all()
# print([r.name for r in res])

# 删除
# session.query(Classes).filter(Classes.id > 2).delete()
# res = session.query(Classes).all()
# for r in res:
#     print(r.id, r.name)

# 修改
# session.query(Classes).update({Classes.name: Classes.name + '099'}, synchronize_session=False)
# res = session.query(Classes).all()
# for r in res:
#     print(r.id, r.name)


# 复杂查询
# res = session.query(Classes).filter(text("id<:idv and name=:namev")).params(idv=2,
#                                                                             namev='Python全栈099099099099').order_by(
#     Classes.id).all()
# for r in res:
#     print(r.id, r.name)

# 原生sql查询
res = session.query(Classes).from_statement(text("select * from classes where id=:idv")).params(idv=2).all()
print([r.name for r in res])
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
