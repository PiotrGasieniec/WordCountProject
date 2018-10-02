from  django.http import HttpResponse
from django.shortcuts import render

import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fullText = request.GET['fullText']

    wordList = fullText.split()

    wordDict = {}

    for word in wordList:
        if word in wordDict:
            #Increase value for existing key
            wordDict[word] += 1
        else:
            #Add key to dictionary
            wordDict[word] = 1

    sortedWords = sorted( wordDict.items(), key=operator.itemgetter(1), reverse=True )

    return render(request, 'count.html', {'fullText': fullText, 'count': len(wordList), "sortedWords": sortedWords })

def about(request):
    return render(request, 'about.html')