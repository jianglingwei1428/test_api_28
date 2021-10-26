#实现用户的增删改查
#1、搭建框架，先定义类和方法，pass占位
#2、填充内容

from apis.base import Base
from loguru import logger
from setting import LOGIN_INFO

class UserManagerApi(Base):  #继承父类

    def __init__(self):
        self.add_path = '/admin/admin/create'
        self.edit_path = '/admin/admin/update'
        self.del_path = '/admin/admin/delete'
        self.get_path = '/admin/admin/list?page=1&limit=20&sort=add_time&order=desc'


    #新增管理员   body里的参数有必填和非必填，所以用可变化参数接收非必填

    def add_user(self,username,password,**kwargs):              #**kwargs :字典形式的可变化参数
        user_url = self.get_url(self.add_path)                   #调用URL方法，拼接新增管理员的URL
        user_data = {'username':username,'password':password}   #定义一个请求体
        if kwargs:                                              #如果可变化参数不为空
            user_data.update(**kwargs)                            #将可变化参数以字典的形式添加到请求体中
        logger.info("新增管理员请求体为{}".format(user_data))
        return self.post(user_url,user_data)                     #调用post方法，返回响应数据


    #编辑管理员

    def edit_user(self,user_id,username,password,**kwargs):
        user_url = self.get_url(self.edit_path)
        user_data = {'id':user_id,'username':username,'password':password}
        if kwargs:
            user_data.update(**kwargs)
            logger.info("编辑管理员的请求体{}".format(user_data))
        return self.post(user_url,user_data)



    #删除管理员

    def delete_user(self,user_id,username,password,**kwargs):
        user_url = self.get_url(self.del_path)
        user_data = {'id':user_id,'username':username,'password':password}
        if kwargs:
            user_data.update(**kwargs)
            logger.info("删除管理员请求体{}".format(user_data))
        return self.post(user_url,user_data)

    #查询管理员

    def get_user(self):
        get_url = self.get_url(self.get_path)
        return self.get(get_url)


