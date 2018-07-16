from django.http import HttpResponse
from django.shortcuts import redirect, render

from lists.models import Item

# Create your views here.

# def home_page(request):
#     if request.method == 'POST':
#         item = Item()
#         item.text = request.POST.get('item_text', '')
#         item.save()
#         return render(request, 'home.html', {
#             'new_item_text': item.text,
#         })
#     return render(request, 'home.html')


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')
    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})