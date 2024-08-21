from django.urls import path
from . import views




urlpatterns = [
    path("", views.base_func, name = "base_func"),

    path("rng/", views.rng, name= "rng"),
    
    path("fags_home/", views.fags_home, name = "fags_home"),
    path("fags_search/", views.fags_search, name = "fags_search"),
    path("fags_add/", views.fags_add, name = "fags_add"),
    
    
    path("fags/<str:fag>/", views.individual_fags, name = "individual_fags"),
    # path("article/<int:year>/", views.year_archive),
    # path('fags/<slug:foo>', views.slug_test),

]