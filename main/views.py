from django.shortcuts import render
from django.http import HttpResponse

import json
from datetime import datetime
import time
import random
# Create your views here.

def get_books(request):
    my_book = {
        1:'Java Book',
        2:'Python Book',
        3:'C++ Book'
    }
    return HttpResponse(json.dumps(my_book))

def index(request):
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(1)
        return HttpResponse(f'<h1>Current Time : {now}<h1>')
        

def get_lottory(request):
    nums = (random.sample(range(1,50),6))
    print(nums)
    s_num = random.randint(1,50)
    num_str = ' '.join(map(str,nums))+f' 特別號:{s_num}'   
    return HttpResponse(f'<h1>{num_str}</h1>')

def get_lottory2(request):
    nums = (random.sample(range(1,50),6))
    s_num = random.randint(1,50)
    num_str = ' '.join(map(str,nums))   
    return render(request,'lottory.html',{'numbers':num_str,'x':s_num})
        

    

