from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('user/', views.user_page, name='user'),
    path('create-question/<int:testID>', views.create_question, name='create-question'),
    path('admin-panel/', views.admin_panel, name='admin'),
    path('create-test/', views.create_test, name='create-test'),
    path('edit-test/<int:testID>', views.edit_test, name='edit-test'),
    path('delete-question/<int:questionID>', views.delete_question, name='delete-question'),
    path('test-already-attempted/', views.err1_page, name='err1'),
    path('user-details/<int:testID>', views.user_details, name='user-details'),
    path('test/', views.test_page, name='test'),
    path('test/get-next-question/<int:questionnum>', views.get_next_question, name='get-next-question'),
    path('test/save-answer', views.save_question, name='save-question'),
    path('test/finish', views.finish_test, name='finish-test'),
    path('test/get-test-status', views.get_test_status, name='get-test-status'),
    path('reset-user/<int:userID>/<int:testID>/', views.reset_user, name='reset-user'),
    path('admin-panel/change-time/', views.set_time, name='change-time'),
    path('upload-question/<int:testID>', views.upload_questions, name='upload-questions'),
    path('upload-users/<int:testID>', views.upload_users, name='upload-users'),
]
