from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')
    # render 함수는 3개의 인자를 받아줄 수 있다. 
    # 3번째 인자는 dic형 자료를 받아올 수 있다.
    