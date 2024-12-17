from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from school.views import AdminView, OfficeStaffView, LibrarianView,AddStudentView,ListStudentsView,UpdateStudentView,DeleteStudentView,FeesHistoryCreateView,FeesHistoryListView,FeesHistoryUpdateView,FeesHistoryDeleteView,LibraryHistoryCreateView,LibraryHistoryListView,LibraryHistoryUpdateView,LibraryHistoryDeleteView

urlpatterns = [
    path('admin-view/', AdminView.as_view(), name='admin-view'),
    path('office-staff-view/', OfficeStaffView.as_view(), name='office-staff-view'),
    path('librarian-view/', LibrarianView.as_view(), name='librarian-view'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # urls for office staff
    path('add-student/', AddStudentView.as_view(), name='add-student'),
    path('list-students/', ListStudentsView.as_view(), name='list_students'),
    path('update-student/<int:pk>/', UpdateStudentView.as_view(), name='update_student'),
    path('delete-student/<int:pk>/', DeleteStudentView.as_view(), name='delete_student'),
    path('add-fees/', FeesHistoryCreateView.as_view(), name='fees-history-create'),
    path('fees-history/', FeesHistoryListView.as_view(), name='fees-history-list'),
    path('fees-history/<int:id>/update/', FeesHistoryUpdateView.as_view(), name='fees-history-update'),
    path('fees-history/<int:id>/delete/', FeesHistoryDeleteView.as_view(), name='fees-history-delete'),

     # urls for librarian
    path('add-library-details/', LibraryHistoryCreateView.as_view(), name='library-history-add'),
    path('library-history/', LibraryHistoryListView.as_view(), name='library-history-list'),
    path('library-history/<int:id>/update/', LibraryHistoryUpdateView.as_view(), name='library-history-edit'),
    path('library-history/<int:id>/delete/', LibraryHistoryDeleteView.as_view(), name='library-history-delete'),
    
]