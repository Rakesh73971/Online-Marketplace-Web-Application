from django.shortcuts import render,get_object_or_404,redirect
from .models import NewItem,Categories
from .forms import NewItemForm,UserRegistrationForm
from django.db.models import Count
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    items = NewItem.objects.all().order_by('-updated')
    categories = Categories.objects.annotate(item_count=Count('newitem')).all()
    return render(request,'home.html',{'items':items,'categories':categories})

@login_required
def add_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST,request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('home')
    else:
        form = NewItemForm()
    return render(request,'item_form.html',{'form':form})

def edit_item(request,item_id):
    item = get_object_or_404(NewItem,pk=item_id,user=request.user)
    if request.method == 'POST':
        form = NewItemForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('home')
    else:
        form = NewItemForm(instance=item)
    return render(request,'item_form.html',{'form':form})

def delete_item(request,item_id):
    item = get_object_or_404(NewItem,pk=item_id,user=request.user)
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    return render(request,'item_delete.html',{'item':item})

def single_item(request,item_id):
    item = NewItem.objects.get(pk=item_id)
    return render(request,'single_item.html',{'item':item})


def browse_items(request, category_id=None):
    categories = Categories.objects.all()

    if category_id:
        items = NewItem.objects.filter(category_id=category_id)
    else:
        items = NewItem.objects.all()

    return render(request, 'browse.html', {
        'items': items,
        'categories': categories,
        'selected_category': category_id,   # optional, for highlighting active category
    })

def my_items(request,user_id):
    items = NewItem.objects.filter(user=user_id)
    return render(request,'dashboard.html',{'items':items})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})
            
