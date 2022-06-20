from django.contrib import messages
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import imageio.v2 as imageio 
import os
from SearchEngine.colordescriptor import ColorDescriptor
from SearchEngine.searcher import Searcher
# Create your views here.

def Home(request):
    context = {}
    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['imageUpload']
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)
            imgQuery = imageio.imread(r'ImageSimilar/static/Data/TestSet' + fs.url(name))
            cd = ColorDescriptor((8, 12, 3))
            features = cd.describe(imgQuery)
            searcher = Searcher("SearchEngine/index.csv")
            results = searcher.search(features)
            context = {'url': fs.url(name), 'results' : results}
            return render(request, 'output.html', context)
            
        except:
            messages.error(request, 'Not File uploaded')
    return render(request, 'input.html', context)
