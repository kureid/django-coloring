from django.shortcuts import render
from .forms import TestForm


def index(request):
    my_dict = {
        'insert1': "本ページは実験用のページです",
        'name': "某ダメ人間",
        'form': TestForm(),
        'insert_forms': '初期値が表示されています   ',
    }

    if request.method == 'POST':
        my_dict['insert_forms'] = '文字列:' + request.POST['text'] + '<br>整数型:' + request.POST['num']
        my_dict['form'] = TestForm(request.POST)

    return render(request, 'webtop/index.html', my_dict)
