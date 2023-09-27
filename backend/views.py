from django.http import HttpResponse

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)

def viewArticle(request, articleId):
   print('ddddd')
   text = "Displaying article Number : %s"%articleId
   return HttpResponse(text)

# def viewArticle(request, month, year):
#    text = "Displaying articles of : %s/%s"%(year, month)
#    return HttpResponse(text)