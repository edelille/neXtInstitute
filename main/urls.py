from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # about page
    #Principal Investigator | Teaching | Research | Service | Statement | Photos | Links
    path('principal-investigator', views.PrincipalInvestigatorView.as_view()),
    path('teaching', views.TeachingView.as_view()),
    path('research', views.ResearchView.as_view()),
    path('service', views.ServiceView.as_view()),
    path('statement', views.StatementView.as_view()),
    path('photos',views.PhotosView.as_view()),
    path('links',views.LinksView.as_view()),
]