from django.shortcuts import render

def main(request):
    return render(request, "main\main.html")
    
def picture(request):
    return render(request, "main\picture.html")