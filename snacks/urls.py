from django.urls import path
from .views import SnackListView, SnackDetailView, SnackCreateView, SnackUpdateView, SnackDeleteView, SnacksApiList, SnackDetail

urlpatterns = [
    # path('', SnackListView.as_view(), name='list_view'),
    path('', SnacksApiList.as_view(), name='snacks_list'),
    path('<int:pk>', SnackDetail.as_view(), name='snacks_detail')
    # path('<int:pk>/', SnackDetailView.as_view(), name='detail_view'),
    # path('create/', SnackCreateView.as_view(), name='create_view'),
    # path('<int:pk>/update/', SnackUpdateView.as_view(), name='update_view'),
    # path('<int:pk>/delete/', SnackDeleteView.as_view(), name='delete_view'),
]
