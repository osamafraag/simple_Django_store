from django.shortcuts import render, redirect,reverse
from store.models import Product
from store.forms import ProductModelForm, SearchForm
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    products = Product.products()
    form = SearchForm()
    if request.POST:
        form = SearchForm(request.POST)
        if form.is_valid():
            name = request.POST['find']
            products = Product.objects.filter(name__startswith=name)
            return render(request, 'store/index.html', context={"products": products, "form":form})
    return render(request, 'store/index.html', context={"products": products,"form":form})

def contactUs(request):
    return render(request, 'store/layouts/contactUs.html')

def aboutUs(request):
    return render(request, 'store/layouts/aboutUs.html')


def details(request, id):
    product = Product.get(id)
    return render(request, 'store/details.html', context={"product":product})
    
    
@login_required()
def delete(request, id):
    product = Product.get(id)
    if product.owner and product.owner.id == request.user.id:
        product.delete()
        return redirect(reverse('index'))
    messages.error(request, 'only owner can delete his product')
    return redirect(product.details_url())

@login_required()
def createViaForm(request):
    form = ProductModelForm()
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save() 
            product.owner = request.user
            product.save()
            return redirect(product.details_url())
    return render(request, 'store/forms/create.html',context={"form": form})

@login_required()
def editViaForm(request, id):
    product = Product.get(id)
    if product.owner and product.owner.id == request.user.id:
        form = ProductModelForm(instance=product)
        if request.method== 'POST':
            form =  ProductModelForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                return redirect(product.details_url())
        return  render(request, 'store/forms/edit.html', context={"form":form})
    messages.error(request, 'only owner can edit his product')
    return redirect(product.details_url())

    

class CreateProduct(View):
    def get(self,request):
        form = ProductModelForm()
        return render(request, 'store/forms/create.html', context={"form": form})

    def post(self, request):
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            product=form.save()
            return redirect(product.details_url())
        return render(request, 'store/forms/create.html',context={"form": form})



class EditProduct(View):
    def get(self,request, id):
        product = Product.get(id)
        form = ProductModelForm(instance=product)
        return render(request, 'store/forms/edit.html',context={"form": form})

    def post(self, request, id):
        product = Product.get(id)
        form = ProductModelForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product=form.save()
            return redirect(product.details_url())
        return render(request, 'store/forms/edit.html', context={"form": form})