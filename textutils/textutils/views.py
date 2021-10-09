from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #params={'name':"sarika",'place':'mumbai'}
    return render(request,'index.html')

def analyze(request):
    djtext =request.POST.get('text','default')
    rempunc = request.POST.get('rempunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover', 'off')
    numberremover=request.POST.get("numberremover","off")

    print(djtext)
    #analyzed=djtext
    if  rempunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = " "
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
                djtext=analyzed
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
    if fullcaps =="on":
        analyzed = " "
        for char in djtext:
            analyzed=analyzed+char.upper()
            djtext = analyzed
        params={'purpose': 'Change To uppercase', 'analyzed_text': analyzed}
       # return render(request,"analyze.html",params)
    if newlineremover=="on":
        analyzed = " "
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
                djtext = analyzed
        params = {'purpose': 'New Line remover', 'analyzed_text': analyzed}
        #return render(request, "analyze.html", params)
    if spaceremover=="on":
        analyzed = ""
        for index, char in enumerate(djtext):
            # It is for if a extraspace is in the last of the string
            if char == djtext[-1]:
                    if not(djtext[index] == " "):
                        analyzed = analyzed + char

            elif not(djtext[index] == " " and djtext[index+1]==" "):                        
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if numberremover == "on":
        analyzed = ""
        numbers = '0123456789'

        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char
        
        params = {'purpose': 'Number Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params)
    if(rempunc != "on" and newlineremover!="on" and spaceremover!="on" and fullcaps!="on" and numberremover != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)

def index2(request):
    return render(request, 'index2.html')