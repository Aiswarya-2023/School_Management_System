from rest_framework import serializers
from school.models import User,Student,LibraryHistory,FeesHistory

class UserSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = ['id','username','role','password']

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

class LibraryHistorySerializer(serializers.ModelSerializer):

    class Meta:

        model = LibraryHistory
        fields = ['student', 'book_title', 'borrowed_date', 'return_date', 'status']

class FeesHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = FeesHistory
        fields = ['student_id', 'fee_type', 'amount', 'payment_date', 'remarks']

    