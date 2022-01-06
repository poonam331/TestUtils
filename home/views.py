#this is created by me
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse('Welcome to Index Page')
    return render(request, 'index.html')

def analyze(request):
    '''Because of 'post' url is clean and not getting input data in url'''
    # djtext = request.GET.get('text', 'default')
    # removepunc = request.GET.get('removepunc', 'off')
    # fullcaps = request.GET.get('fullcaps', 'off')
    # newlineremover = request.GET.get('newlineremover', 'off')
    # extraspaceremover = request.GET.get('extraspaceremover', 'off')
    # charactercounter = request.GET.get('charactercounter', 'off')
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)  
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        # print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)   
    if charactercounter == 'on':
        # analyzed = len(djtext)        
        analyzed = len(djtext) - djtext.count(' ')
        params = {'purpose': 'Character Counter', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)  

    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)   
    # else:
    #     return HttpResponse('Error !!!!!')

# def ex1_sites(request):
#     sites = '''<h2>Navigation Bar </h2>
#     <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
#     <a href="https://www.facebook.com/"> Facebook </a> <br>
#     <a href="https://www.flipkart.com/"> Flipkart </a> <br>
#     <a href="https://www.hindustantimes.com/"> News </a> <br>
#     <a href="https://www.google.com/"> Google </a> <br>'''
#     return HttpResponse(sites)

# def removepunc(request):
#     return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newline remove first")


# def spaceremove(request):
#     return HttpResponse("space remover back")

# def charcount(request):
#     return HttpResponse("charcount ")