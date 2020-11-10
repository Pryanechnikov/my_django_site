from django.shortcuts import render
from .models import Assortment
from .forms import AssortmentForm
from django.shortcuts import redirect
from .models import Order

def pp(request):
 orders = Order.objects.order_by('date',)
 return render(request, 'my_app/pp.html',{ 'orders':orders})

def start(request):
 assortments = Assortment.objects.order_by('created_date',)
 return render(request, 'my_app/start.html',{ 'assortments':assortments})


def post_list(request):
 assortments = Assortment.objects.order_by('created_date')
 return render(request, 'my_app/post_list.html', {'assortments': assortments})

def post_new(request):
 form = AssortmentForm()
 return render(request, 'my_app/post_edit.html',{'form': form})

def post_new(request):
 if request.method == "POST":
    form = AssortmentForm(request.POST)
    if form.is_valid():
       Assortment = form.save(commit=False)
       Assortment.Editor = request.user
       Assortment.created_date = timezone.now()
       Assortment.save()
       return redirect('post_list')
 else:
    form = AssortmentForm()
 return render(request, 'blog/post_edit.html',{'form': form})

 

