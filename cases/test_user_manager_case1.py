#主要实现的是用户管理的测试用例

import unittest
from apis.user_manager_api import UserManagerApi
from data.user_manager_data import user_manager_data



class TestUserManagerTest(unittest.TestCase):

    user_id = 527 #id来自于添加管理员后的响应数据

    @classmethod
    def setUpClass(cls) -> None: #每次实例化一个用户管理的对象
        cls.user = UserManagerApi()


    # 实现添加测试用例 (肯定需要调用添加管理员的接口)
    # @unittest.skip('此条不执行')
    def test01_add_user(self):
        #1、定义数据

        #2、调用添加管理员接口
        result = self.user.add_user(user_manager_data['username'],user_manager_data['password'])
        #将获取到的ID赋值给类变量user_id
        if result.get("data").get("id"):
            TestUserManagerTest.user_id = result.get("data").get("id")
        #3、断言
        self.assertEqual(0,result.get('errno'))


    #实现编辑测试用例
    #
    def test02_edit_user(self):
        #1、定义数据

        #2、调用编辑接口
        result = self.user.edit_user(TestUserManagerTest.user_id,user_manager_data['newusername'],user_manager_data['password'])
        #注意类变量user_id的写法，要通过类名调用
        #3、进行断言
        self.assertEqual(0,result.get('errno'))



    #实现删除测试用例
    def test04_delete_user(self):

        # 2、调用删除接口
        result = self.user.delete_user(TestUserManagerTest.user_id, user_manager_data['newusername'], user_manager_data['password'])
        # 注意类变量user_id的写法，要通过类名调用
        # 3、进行断言
        self.assertEqual(0, result.get('errno'))



    #实现查询测试用例

    def test03_get_user(self):
        result = self.user.get_user()
        self.assertEqual(0, result.get('errno'))
