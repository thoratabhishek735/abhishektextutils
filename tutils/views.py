# I have created this site
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    #return HttpResponse("Abhi home") or and using templtes see below line
    return render(request,'index.html')

def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off') #default made off to detect checkbox is off
    fullcaps=request.POST.get('fullcaps','off')
    newlineremove=request.POST.get('newlineremove','off')
    if (removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for i in djtext:
            if i not in punctuations:
                analyzed=analyzed+i

        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed


    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
        djtext=analyzed


    if (newlineremove == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char != '\r':
               analyzed = analyzed +  char
        params = {'purpose': 'removed new line', 'analyzed_text': analyzed}
        djtext=analyzed


    return render(request, 'analyze.html', params)











#def capitalize(request):
   # return HttpResponse("capitalize first")
#def newlineremove(request):
   # return HttpResponse("capitalize first")


#def spaceremove(request):
    #return HttpResponse("space remover")

#def charcount(request):
    #return HttpResponse("charcount ")