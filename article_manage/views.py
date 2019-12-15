from django.shortcuts import render, redirect

from django.shortcuts import HttpResponse
from django.urls import reverse
from django.utils.http import urlencode

from dao import CategoryDao
from dao import ItemDao
import dao
from models import Category
from models import Item
# Create your views here.


category_dao = CategoryDao()
item_dao = ItemDao()


def index(request):
    """

    :param request:
    :return:
    """
    return render(request, "index.html")


def list_category(request):
    """
    获取文章目录列表
    :param request:
    :return:
    """
    if request.method == "GET":
        c_name = request.GET.get("c_name")
        category_list = None
        if c_name is None:
            category_list = category_dao.list()
        else:
            param_dict = dict()
            param_dict['c_name'] = c_name
            print('根据条件查询')
        dict_category = {"category_list": category_list}
    return render(request, "list_category.html", dict_category)


def pre_add_category(request):
    """

    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "add_category.html")


def add_category(request):
    """
    添加一个类目
    :param request:
    :return:
    """
    if request.method == "POST":
        c_name = request.POST.get("c_name")
        c_desc = request.POST.get("c_desc")
        category_model = Category(0, c_name, c_desc)
        result = category_dao.save(category_model)
    return redirect("/list_category")


def delete_category(request):
    """
    删除一个类目
    :param request:
    :return:
    """
    if request.method == "GET":
        c_id = request.GET.get("c_id")
        category_dao.delete_by_id(c_id)
    return redirect("/list_category")


def pre_add_item(request):
    """

    :param request:
    :return:
    """
    if request.method == "GET":
        c_id = request.GET.get("c_id")
        param = {"c_id": c_id}
        return render(request, "add_item.html", param)


def add_item(request):
    """
    添加一篇文章
    :param request:
    :return:
    """
    if request.method == "POST":
        i_content = request.POST.get("i_content")
        c_id = request.POST.get("c_id")
        i_title = request.POST.get("i_title")
        item_model = Item(0, i_title, i_content, c_id)
        item_dao.save(item_model)

        return render(request, "index.html")


def delete_item(request):
    """
    删除文章
    :param request:
    :return:
    """
    if request.method == "GET":
        i_id = request.GET.get("i_id")
        if i_id is not None:
            item_dao.delete_by_id(i_id)
            return render(request, "index.html")


def list_item(request):
    """
    根据类目id列出其包含的文章列表
    :param request:
    :return:
    """
    item_list = None
    if request.method == "GET":
        c_id = request.GET.get("c_id")
        if c_id is not None:
            item_list = item_dao.list_by_cid(c_id)
        else:
            pass
        for item in item_list:
            item['i_content'] = item['i_content'].split('。')[0]
        item_list = {"item_list": item_list}
    else:
        pass
    return render(request, "list_item.html", item_list)


def show_item_detail(request):
    """
    查看文章详细
    :param request:
    :return:
    """
    if request.method == "GET":
        i_id = request.GET.get("i_id")
        if i_id is not None:
            item_detail = item_dao.get_by_id(i_id)
            item_detail = {"item_detail": item_detail}
            return render(request, "item_detail.html", item_detail)



