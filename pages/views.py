from django.shortcuts import render, redirect

from pages.models import ContactModel


def home_page_view(request):
    return render(request, 'home.html')


def contact_page_view(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        new_contact = ContactModel.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        new_contact.save()
        return redirect('pages:contact')
    else:
        return render(request, 'contact.html')


def product_page_view(request):
    return render(request, 'product-list.html')


def about_page_view(request):
    return render(request, 'about-us.html')


def blog_page_view(request):
    blogs = BlogModel
    return render(request, 'blog-list.html')
