from django.urls import path
from . import views

urlpatterns = [
    path('fundraisers/', views.FundraiserListView.as_view()),
    path('fundraisers/<int:pk>/', views.FundraiserDetailView.as_view()),
    path('pledges/', views.PledgeListView.as_view()),
    path('pledges/<int:pk>/', views.PledgeDetailView.as_view()),   
]