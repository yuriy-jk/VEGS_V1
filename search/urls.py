from django.urls import path


from search.views import UserSearchListView


urlpatterns = [
    path('searchlist/', UserSearchListView.as_view(), name='searchlist')
]

