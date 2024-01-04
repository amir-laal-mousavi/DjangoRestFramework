from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', views.TodosViewSetApiView)


urlpatterns = [
  # path('', views.all_todos),
  # path('<int:todo_id>', views.todo_detail_view),
  # path('cbv/', views.ManageTodosApiView.as_view()),
  # path('cbv/<int:todo_id>', views.TodosDetailApiView.as_view()),
  # path('mixins/', views.TodosListMixinApiView.as_view()),
  # path('mixins/<pk>', views.TodosDetailMixinApiView.as_view()),
  path('', views.TodosListGenericApiView.as_view()),
  path('<pk>', views.TodosDetailGenericApiView.as_view()),
  path('viewsets/', include(router.urls)),
  path('users/', views.UsersGenericApiView.as_view()),
]

