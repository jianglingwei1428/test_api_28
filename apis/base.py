'''
主要实现的是基础的接口请求，例如最基本的get，post,header,url
'''
import requests

import setting

from loguru import logger
from cacheout import Cache
cache = Cache()   #通过类Cache创建一个对象，通过对象调set/get方法设置缓存和提取缓存


#定义类

class Base(object):




    # 实现URL的方法
    #path:接口路径
    #params:查询字符串
    #return: 返回url


    def get_url(self,path,params=None):
        if params:  #如果params不为空
            return setting.BASE_URL + path + '?'+params
        return setting.BASE_URL +path


    # 实现get方法
    # params url :url地址
    # return :  返回请求响应体(接收json类型，json接收只有响应体)

    def get(self,url):
        try:
            response = requests.get(url,headers = self.get_headers())
            result = response.json()
            logger.info("请求get数据：{}".format(result))
            return result
        except Exception as e:
            logger.error("请求get方法失败，返回数据{}".format(e))



    # 实现post方法
    # params url :url地址
    # params data: 请求体
    # return :  返回请求响应体

    def post(self, url,data):

        try:
            response = requests.post(url,json = data, headers = self.get_headers()) #该项目所有的请求体都为JSON类型，所以利用JSON传参
            result = response.json()
            logger.info("请求post数据：{}".format(result))
            return result
        except Exception as e:
            logger.error("请求post方法失败，返回数据{}".format(e))


    #定义登录

    def login(self,username,password):
        login_path = '/admin/auth/login'
        login_url = self.get_url(login_path)
        login_data = {'username':username,'password':password}
        result = self.post(login_url,login_data)

        try:
            if result.get("errno") == 0:  #断言响应数据，如果错误为0即为登录成功，正确信息都是从接口文档中获得的，
                logger.info("请求登录接口成功")
                token = result.get('data').get('token')
                cache.set('token',token)   #将token值加入缓存
            else:
                logger.error("请求登录接口失败:{}".format(result))
        except Exception as e:
            logger.error("请求接口登录异常，异常数据{}".format(e))


    #请求头
    def get_headers(self):
        headers = {'Content-Type':'application/json'}
        token = cache.get('token')
        if token: #如果token值不为空
            headers.update({'X-Litemall-Admin-Token':token}) #将token键值对加入字典headers,注意加入的格式是JSON（）字典格式
        logger.warning("请求头信息返回数据：{}，提示：多个接口需要用到token值".format(headers))
        return headers






if __name__ == '__main__':

    b =Base()
    print(b.get_url('/admin/admin/update'))
    print(b.get_url('/admin/admin/update','limit=20&sort=add_time&order=desc'))
    print(b.get('http://www.weather.com.cn/data/sk/101010100.html'))















