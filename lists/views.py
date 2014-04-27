from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    if request.method == 'POST':
        new_item = request.POST['item_text']
    else:
        new_item = ''

    return render(request, 'home.html', {'new_item_text': new_item})
