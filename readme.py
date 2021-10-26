'''
接口自动化

一、实现步骤

1、先实现apis里的内容

    * base ： 就是提供给被测接口的一个基类
        *grt_url（）：主要处理URL
        *get（） ： 就是将request.get()方法进行重写，使其更便捷更符合需求
        *post（） ： 就是将request.post()方法进行重写，使其更便捷更符合需求
        *get_hesders():获取请求头中的数据
        *login（） ： 调用登录接口，将token值保存到缓存

    * user_mangager_api :主要实现的是用户管理员接口（在实现接口时，尽量将接口归类：将相同类型的接口定义在一个类中。
    以减少文件数量，提高效率；一个接口一个类或者模块太过冗余）
        *add_user :添加管理员
        *edit_user :编辑管理员
        *delete_user ；删除管理员
        *get_user :查询管理员

2、实现测试用例






























        '''
