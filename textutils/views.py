# This is cretaed by Piyush

from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''<h1>Welcome piyush</h1>
#                      <a href="https://www.google.com/">GOOGLE</a>''')
#
# def about(request):
#     return HttpResponse("Hello launde")


def index(request):
    params = {'name':'harray', 'place' : 'mars'}
    return render(request,'index.html',params)


def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    fullcaps=request.GET.get('fullcaps','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != '\n':
                analyzed = analyzed + char
        params = {'purpose': 'NEW LINEREMOVED', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'NEW LINEREMOVED', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    elif(fullcaps=='on'):
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'UPPERCASE', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    else:
        return HttpResponse('Error check the checkbox')

def removepunc(request):
    return HttpResponse('''remove punc''')

def capfirst(request):
    return HttpResponse('''capatalize first''')

def newlineremove(request):
    return HttpResponse('''newline remove first''')

def spaceremove(request):
    return HttpResponse('''space remover''')

def charcount(request):
    return HttpResponse('''char count''')
