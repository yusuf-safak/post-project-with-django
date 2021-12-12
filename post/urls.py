from django.urls import path
from post.views import *

urlpatterns = [
    path('',postlist_view),
    path('create/', create_view),
    path('fillForm/', fillForm_view),
    path('delete/<int:id>', delete_view),
    path('update/<int:id>', update_view),
    path('sendUpdate/<int:id>', update_view),
    path('detail/<int:id>', detail_view),
]
