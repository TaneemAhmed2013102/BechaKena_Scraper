from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("taneem", views.taneem, name="taneem"),
    path("books_shelf", views.books_shelf, name="books_shelf"),
    path("scrape_rokomari",
         views.scrape_rokomari, name="booklist"),
    path("scrape_boibitan",
         views.scrape_boibitan, name="booklist"),


# FOR MORE SCRAPING PURSPOSES I HAVE CREATED THE LOWER PATHS!

#     path("books_list", views.books_list, name="booklist"),
#     path("books_list2", views.books_list2, name="booklist2"),
#     path("doctor", views.doctor, name="doctors"),
#     path("doctors_list", views.doctors_list, name="doctorslist"),
#     path("urology", views.urology, name="urology"),
#     path("neurology", views.neurology, name="neurology"),
#     path("dermatology", views.dermatology, name="dermatology"),
#     path("anesthesilogy", views.anesthesilogy, name="anesthesilogy"),
#     path("cardiac_Surgery", views.cardiac_Surgery, name="cardiac_Surgery"),
#     path("cardiology", views.cardiology, name="cardiology"),
#     path("ent", views.ent, name="ent"),
#     path("scrape_doctors",
#          views.scrape_doctors, name="doctorslist"),
#     path("scrape_doctorsSquare",
#          views.scrape_doctorsSquare, name="doctorslist"),
     
]
