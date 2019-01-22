from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext'] #text 라는 변수에 입력한 원문의 전체가 담김
    words = text.split() # text를 공백기준으로 나눠서 words라는 리스트에 넣음
    word_dictionary = {} # <단어 : 몇번 단어 : 몇번 > 이렇게 저장되있음
    #사전형 자료형에서 쌍을 보내주는 파이썬 상의 문법 => items

    for word in words: #word 는 반복문변수, words는 리스트에 해당
        if word in word_dictionary: #word가 word_dictionary에 있는 값이라면
            #increase
            word_dictionary[word]+=1
        else:
            #add to dictionary
            word_dictionary[word] =1

    return render(request, 'result.html', {'full' : text, 'totalcount':len(words), 'dictionary':word_dictionary.items()} ) # 키값(임의로 쓰는거) : value(받아올 내용)
