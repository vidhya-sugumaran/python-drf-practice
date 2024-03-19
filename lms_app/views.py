from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import LMS
from .forms import BookForm

def welcome(request):
    return HttpResponse('Welcome to first lms app using Django')

def add_book(request):
    data = {}
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, 'add_book.html', data)

def list_books(request):
    data = {}
    data['books'] = LMS.objects.all()
    return render(request, 'list_books.html', data)

def view_book(request, id):
    data = {}
    data['book'] = LMS.objects.get(id = id)
    return render(request, 'view_book.html', data)

def update_book(request, id):
    data = {}
    obj = get_object_or_404(LMS, id = id)
    form = BookForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/library/update_book/'+ id)
    data['form'] = form
    return render(request, 'update_book.html', data)

def delete_book(request, id):
    obj = get_object_or_404(LMS, id = id)
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect('Deleted')
    return render(request, 'delete_book.html')
