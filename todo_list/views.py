from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
	if request.method == 'POST':
		form = ListForm(request.POST or None)
		#check how to best validate this form...this has to be safer
		form.save()
		messages.success(request,('Item has been added into the list'))
		all_items = List.objects.all
		return render(request,'home.html',{'all_items':all_items})
	else:
		all_items = List.objects.all
		return render(request,'home.html',{'all_items':all_items})



def about(request):
	my_name= "Manny Dash"
	name = my_name.split(" ")
	context = {'first_name':name[0],'last_name':name[1]}
	return render(request,'about.html',context)


def delete(request, list_id):
	item_to_delete = List.objects.get(pk=list_id)
	item_to_delete.delete()
	messages.success(request,('Item has been removed from the list'))
	return redirect('home')


def complete(request,list_id):
	item_to_complete = List.objects.get(pk=list_id)
	item_to_complete.completed = True
	item_to_complete.save()
	messages.success(request,('Item ' +list_id+ ' has been completed'))
	return redirect('home')


def uncomplete(request,list_id):
	item_to_uncomplete = List.objects.get(pk=list_id)
	item_to_uncomplete.completed = False
	item_to_uncomplete.save()
	messages.success(request,('Item ' +list_id+ ' has been set back to Not completed'))
	return redirect('home')

def edit(request, list_id):
	if request.method == 'POST':
		item = List.objects.get(pk=list_id)
		form = ListForm(request.POST or None, instance = item)
		#check how to best validate this form...this has to be safer
		form.save()
		messages.success(request,('Item has been updated'))
		return redirect('home')
	else:
		item = List.objects.get(pk=list_id)
		return render(request,'edit.html',{'item':item})



