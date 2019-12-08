from django.db import models

# Create your models here.


class Category(object):

    def __init__(self, c_id, c_name, c_desc):
        self.__c_id = c_id
        self.__c_name = c_name
        self.__c_desc = c_desc

    def __str__(self):
        return 'c_id:{}，c_name:{}，c_desc:{}'.format(self.__c_id, self.__c_name, self.__c_name)

    def get_name(self):
        return self.__c_name

    def get_desc(self):
        return self.__c_desc

    def get_cid(self):
        return self.__c_id


class Item(object):

    def __init__(self, i_id, i_title, i_content, i_cid):
        self.__i_id = i_id
        self.__i_content = i_content
        self.__i_cid = i_cid
        self.__i_title = i_title

    def get_id(self):
        return self.__i_id

    def get_content(self):
        return self.__i_content

    def get_cid(self):
        return self.__i_cid

    def get_title(self):
        return self.__i_title






