from django.shortcuts import render, redirect,reverse
from categories.models import Category
from categories.forms import CategoryModelForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView



class CategoriesList(ListView):
    model = Category
    template_name = 'categories/index.html'
    context_object_name = 'categories'
class CategoryDetails(DetailView):
    model = Category
    template_name = 'categories/details.html'
class CategoryUpdate(UpdateView):
    model = Category
    template_name = 'categories/forms/edit.html'
    form_class = CategoryModelForm
    success_url = reverse_lazy('category.index')
class CategoryCreate(CreateView):
    model = Category
    template_name = 'categories/forms/create.html'
    form_class = CategoryModelForm
    success_url = reverse_lazy('category.index')
class CategoryDelete(DeleteView):
    model = Category
    template_name = 'categories/forms/delete.html'
    success_url = reverse_lazy('category.index')

def index(request):
    categories = Category.categories()
    return render(request, 'categories/index.html', context={"categories":categories})
def details(request, id):
    category = Category.get(id)
    return render(request, 'categories/details.html', context={"category":category})

def delete(request, id):
    category = Category.get(id)
    category.delete()
    return render(request, 'categories/index.html', context={"categories":Category.categories()})


def create(request):
    form = CategoryModelForm()
    if request.POST:
        form = CategoryModelForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            return redirect(category.details_url())
    return  render( request, 'categories/forms/create.html', context={"form": form})

def edit(request, id):
    category = Category.get(id)
    form = CategoryModelForm(instance=category)
    if request.POST:
        form = CategoryModelForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect(category.details_url())
    return render(request, 'categories/forms/edit.html', context={"form":form})