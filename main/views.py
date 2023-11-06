from django.shortcuts import render
from django.http import HttpResponse
from tools import get_chrome, getSoup
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By
import json
from datetime import datetime
import time
import random
from threading import Thread
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from linebot import LineBotApi, WebhookHandler, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage
# Create your views here.
url = 'https://www.manhuaren.com/search/'
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parse = WebhookParser(settings.LINE_CHANNEL_SECRET)


def get_books(request):
    my_book = {
        1: 'Java Book',
        2: 'Python Book',
        3: 'C++ Book'
    }
    return HttpResponse(json.dumps(my_book))


def index(request):
    global url
    datas = quick_pick_comic(url)
    context = {}
    for data in datas:
        context['title'] = data[0]
        context['new_update'] = data[1]
        context['comic_url'] = data[2]
        context['img_url'] = data[-1]
        print(context)
        return render(request, 'index.html', locals())


def quick_pick_comic(url):
    datas = []
    chrome = get_chrome(url)
    comic_xpath = '/html/body/ul[1]/li[1]/a'
    chrome.find_element(By.XPATH, comic_xpath).click()
    soup = BeautifulSoup(chrome.page_source, 'lxml')
    if soup != None:
        content = soup.find('ul', class_="manga-list-2").findAll('li')
    try:
        for comic in content:
            title = [title.text.strip() for title in comic][3]
            new_update = [title.text.strip() for title in comic][-2]
            comic_url = 'https://www.manhuaren.com'+comic.find('a').get('href')
            img_url = comic.find('img').get('src')
            datas.append([title, new_update, comic_url, img_url])
    except Exception as e:
        print(e)
    finally:
        if chrome != None:
            chrome.close()
    return datas


def get_lottory(request):
    nums = (random.sample(range(1, 50), 6))
    print(nums)
    s_num = random.randint(1, 50)
    num_str = ' '.join(map(str, nums))+f' 特別號:{s_num}'
    return HttpResponse(f'<h1>{num_str}</h1>')


def get_lottory2(request):
    nums = (random.sample(range(1, 50), 6))
    s_num = random.randint(1, 50)
    num_str = ' '.join(map(str, nums))

    return render(request, 'lottory.html', {'numbers': num_str, 'x': s_num})
