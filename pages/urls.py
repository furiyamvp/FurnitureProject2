from .views import home_page_view, contact_page_view, blog_page_view, product_page_view, about_page_view
from django.urls import path

app_name = "pages"

urlpatterns = [
    path("", home_page_view, name="home"),
    path("contact/", contact_page_view, name="contact"),
    path("blog/", blog_page_view, name="blogs"),
    path("about/", about_page_view, name="about")
]
