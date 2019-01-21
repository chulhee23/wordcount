from django.shortcuts import render
import operator
# Create your views here.

def home(request):
    return render(request, 'home.html')
    # render 함수는 3개의 인자를 받아줄 수 있다. 
    # 3번째 인자는 dic형 자료를 받아올 수 있다.

def about(request):
    return render(request, 'about.html')
     
def result(request):
    text = request.GET['fulltext']
    
    # word는 리스트자료형으로 넘어간다.

    words = text.split()
    # 총 단어수 = list의 길이

    # 빈 딕셔너리 정의
    word_dic = {}

    for word in words:
        if word in word_dic:
            word_dic[word]+=1
        else:
            # add to dic
            word_dic[word]=1

    # 문장으로 구분하기
    # word안에 마침표가 찍혀있다면 마침표로 br해주겠다.
    
    # 출력할 때 가중치가 0과 1로 존재하니까
    # 0일 경우 <br>태그 추가해주자!
    
    word_w=[] # 딕셔너리를 아이템으로 갖는 리스트
   
    ##### word_w 사용 
    for word in words:
        if ((word.find('.')!=-1) or (word.find('!')!=-1) or (word.find('?')!=-1) ): # 마침표가 있는 경우
            word_w.append({word : 0})
            
        else:  # 없는 경우
            word_w.append({word : 1})
    

    # 단어 숫자순 정렬

    # word_dic은 word : num 으로 구성되어있음
    # operator.itemgetter(1)는 객체의 1번 항목을 받아온다. 
    sorted_dic = sorted(word_dic.items(), key=operator.itemgetter(1))
    # sorted(iterable, key, reverse)
    # param iterable
    # Return a new list containing all items from the iterable in ascending order.
    # A custom key function can be supplied to customize the sort order, and the
    # reverse flag can be set to request the result in descending order.

    return render(request, 'result.html', {
                                            'full':text, 
                                            'total':len(words), 
                                            'dic' : word_dic.items(),
                                            'sorted_dic' : sorted_dic ,
                                            'word_w' : word_w,
                                            })
