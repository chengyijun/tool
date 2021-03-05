# 导入:
import datetime

from sqlalchemy import Column, String, create_engine, Integer, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
from sqlalchemy.orm import relationship

Base = declarative_base()


# 自定义model，必须继承Base类
class Student(Base):
    # 表的名字:
    __tablename__ = 'student'
    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32), nullable=False, unique=True)
    password = Column(String(64), nullable=False)
    ctime = Column(DateTime, default=datetime.datetime.now)
    # 外键
    class_id = Column(Integer, ForeignKey('classes.id'))
    # 索引
    __table_args__ = (
        # 联合唯一索引
        UniqueConstraint('id', 'username', name='uix_id_username'),
        # 普通联合索引
        # Index('ix_id_name','id', 'username')
    )
    # relationship
    belong_classes = relationship('Classes', backref='stus')


class Classes(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False, unique=True)


class hobby(Base):
    # 表的名字:
    __tablename__ = 'hobby'
    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    caption = Column(String(64), default='篮球')


class Student2Hobby(Base):
    # 表的名字:
    __tablename__ = 'student2bobby'

    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    hobby_id = Column(Integer, ForeignKey('hobby.id'))


def init_db():
    """
    根据类创建数据库表
    :return:
    """
    engine = create_engine(
        'mysql+pymysql://abel:abel@192.168.10.194:3333/flask?charset=utf8',
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )

    Base.metadata.create_all(engine)


def drop_db():
    """
    根据类删除数据库表
    :return:
    """
    engine = create_engine(
        'mysql+pymysql://abel:abel@192.168.10.194:3333/flask?charset=utf8',
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )

    Base.metadata.drop_all(engine)


def main():
    # 创建表
    init_db()
    # 删除表
    # drop_db()


if __name__ == '__main__':
    main()
