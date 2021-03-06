from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/api/book/
    path('rank/', views.BookRankView.as_view()),
    path('recommend/', views.BookRecommendView.as_view()),
    path('isbn/', views.IsbnView.as_view()),
    path('favorite/', views.FavoriteView.as_view()),
    path('favorite/del/', views.FavoriteDelView.as_view()),
    path('favorite/search/', views.FavoriteSearchView.as_view()),
    path('favorite/is/', views.IsFavoriteView.as_view()),
    path('douban/kids/', views.KidsBookView.as_view()),
    path('search/',views.SearchView.as_view()),
]