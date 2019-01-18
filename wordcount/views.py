from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')
    # render 함수는 3개의 인자를 받아줄 수 있다. 
    # 3번째 인자는 dic형 자료를 받아올 수 있다.

def about(request):
    return render(request, 'about.html')
     
def result(request):
    text = request.GET['fulltext']
    words = text.split()
    # 총 단어수 = list의 길이

    word_dic = {}

    for word in words:
        if word in word_dic:
            word_dic[word]+=1
        else:
            # add 2 dic
            word_dic[word]=1

    return render(request, 'result.html', { 'full':text, 'total':len(words), 'dic' : word_dic.items() } )
