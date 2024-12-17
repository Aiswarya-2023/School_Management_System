from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from school.permissions import IsAdmin, IsOfficeStaff, IsLibrarian

class AdminView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        return Response({"message": "Welcome, Admin!"})

class OfficeStaffView(APIView):
    permission_classes = [IsAuthenticated, IsOfficeStaff]

    def get(self, request):
        return Response({"message": "Welcome, Office Staff!"})

class LibrarianView(APIView):
    permission_classes = [IsAuthenticated, IsLibrarian]

    def get(self, request):
        return Response({"message": "Welcome, Librarian!"})





# Add student details view
# ========================


from school.serializers import StudentSerializer
from school.models import Student
from rest_framework import status


class AddStudentView(APIView):
    
    permission_classes = [IsAuthenticated, IsOfficeStaff] #Access Officestaff

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# List all Students view
# ======================


from rest_framework.generics import ListAPIView

class ListStudentsView(ListAPIView):
    queryset = Student.objects.all()  # Fetch all student records
    serializer_class = StudentSerializer  # Use the defined serializer



# Update student details
# ====================== 

from rest_framework.generics import RetrieveUpdateAPIView
from school.permissions import IsOfficeStaff  #Restrict access to staff

class UpdateStudentView(RetrieveUpdateAPIView):

    queryset = Student.objects.all()  # Query all students
    serializer_class = StudentSerializer  # Use the update serializer
    permission_classes = [IsAuthenticated, IsOfficeStaff]  #  Require authentication

    def update(self, request, *args, **kwargs):
        """
        Override the update method to provide custom success and error messages.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()  # Retrieve the specific student instance
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        
        # Perform the update
        self.perform_update(serializer)

        # Custom success message
        return Response(
            {"message": "Student details updated successfully!", "data": serializer.data},
            status=status.HTTP_200_OK
        )

    def handle_exception(self, exc):
        """
        Handle exceptions to return custom error messages.
        """
        if isinstance(exc, PermissionError):
            return Response(
                {"message": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().handle_exception(exc)





# Delete student view
# ===================


from rest_framework.generics import DestroyAPIView

class DeleteStudentView(DestroyAPIView):

    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated, IsOfficeStaff]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Student deleted successfully"}, status=status.HTTP_200_OK)
    




# Add fees details of the student view
# ====================================

from school.models import FeesHistory
from school.serializers import FeesHistorySerializer

class FeesHistoryCreateView(APIView):

    permission_classes = [IsAuthenticated,IsOfficeStaff]  # Ensures the user is authenticated

    def post(self, request):
        serializer = FeesHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# List all fees details view
# ========================== 


class FeesHistoryListView(ListAPIView):

    queryset = FeesHistory.objects.all()
    serializer_class = FeesHistorySerializer
    permission_classes = [IsAuthenticated,IsOfficeStaff]  # Ensure the user is authenticated (staff should be authenticated)


    def get_queryset(self):
        
        queryset = FeesHistory.objects.all()
        student_id = self.request.query_params.get('student_id', None)
        if student_id is not None:
            queryset = queryset.filter(student_id=student_id)
        return queryset





# Update fees history views
# =========================


class FeesHistoryUpdateView(RetrieveUpdateAPIView):

    queryset = FeesHistory.objects.all()
    serializer_class = FeesHistorySerializer
    permission_classes = [IsAuthenticated,IsOfficeStaff]  # Ensure the user is authenticated (staff should be authenticated)
    lookup_field = 'id'  # Use 'id' in the URL to specify which record to delete



# Delete fees history
# ===================


class FeesHistoryDeleteView(DestroyAPIView):

    queryset = FeesHistory.objects.all()
    serializer_class = FeesHistorySerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated (staff should be authenticated)
    lookup_field = 'id'  # Use 'id' in the URL to specify which record to delete

    def destroy(self, request, *args, **kwargs):
        # Call the default destroy method to delete the object
        response = super().destroy(request, *args, **kwargs)
        
        # Modify the response to include a success message
        response.data = {'message': ' Deleted successfully'}
        
        return response




# Create library details of the students views
# ============================================


from rest_framework.generics import CreateAPIView
from school.models import LibraryHistory
from school.serializers import LibraryHistorySerializer


class LibraryHistoryCreateView(CreateAPIView):

    queryset = LibraryHistory.objects.all()
    serializer_class = LibraryHistorySerializer
    permission_classes = [IsAuthenticated, IsLibrarian] 



# List library history views
# ==========================

class LibraryHistoryListView(ListAPIView):

    queryset = LibraryHistory.objects.all()  # Retrieve all library history records
    serializer_class = LibraryHistorySerializer  # Serialize the library history data
    permission_classes = [IsAuthenticated,IsLibrarian]  # Ensure the user is authenticated




# update library history views
# ============================


from rest_framework.generics import UpdateAPIView


class LibraryHistoryUpdateView(UpdateAPIView):

    queryset = LibraryHistory.objects.all()
    serializer_class = LibraryHistorySerializer
    permission_classes = [IsAuthenticated,IsLibrarian]
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        # Call the parent's update method to update the object
        partial = kwargs.pop('partial', False)  # If it's a partial update
        instance = self.get_object()  # Get the current instance to update
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        
        # Validate and save the updated data
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"detail": "Library history updated successfully."}, 
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )




# Delete view for delete library details
# ======================================


class LibraryHistoryDeleteView(DestroyAPIView):

    queryset = LibraryHistory.objects.all()  # All LibraryHistory records
    serializer_class = LibraryHistorySerializer  # Use the existing serializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated (eg: librarian)
    lookup_field = 'id'  # Use 'id' to specify which record to delete

    def destroy(self, request, *args, **kwargs):
        # Call the parent's destroy method to delete the object
        response = super().destroy(request, *args, **kwargs)
        
        # Custom message after successful deletion
        return Response(
            {"detail": "Library history deleted successfully."}, 
            status=status.HTTP_204_NO_CONTENT
        )
