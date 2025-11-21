from django.urls import path
from .views import home,list_students, create_student, update_student, delete_student
from .view_cbv import StudentListCreateView, StudentDetailView,StudentSearchView

# urlpatterns=[
#     path('',home,name="home"),
#     path('lists/',StudentListCreateView.as_view(),name='list_students'),
#     path('add/', create_student, name='add_student'),
#     path('update/',update_student),
#     path('delete/',delete_student)
# ]

# # from django.urls import path
# # from .view_cbv import StudentListCreateView, StudentDetailView

# urlpatterns = [
#     path('', StudentListCreateView.as_view(), name='student_list_create'),
#     path('<str:index_number>/', StudentDetailView.as_view(), name='student_detail'),
#     path('search/', StudentSearchView.as_view(), name='student_search'),
# ]


from django.urls import path
from . import views_web as web_views

app_name = "students"

urlpatterns = [
    path('', web_views.student_list, name='student_list'),
    path('create/', web_views.student_create, name='student_create'),
    path('update/<str:index_number>/', web_views.student_update, name='student_update'),
    path('<str:index_number>/', web_views.student_detail, name='student_detail'),  # optional
    path('delete/<str:index_number>/', web_views.student_delete, name='student_delete'),

]
