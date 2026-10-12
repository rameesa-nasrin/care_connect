from django.shortcuts import render

from django.contrib.auth.models import User


from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import authentication,permissions


from staff.models import Doctor

from staff_v2.serializers import DoctorSerializer,UserSerializer


# Create your views here.
class DoctorsListCreateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def get(self,request):

        qs=Doctor.objects.all()

        serializer_instance=DoctorSerializer(qs,many=True)

        return Response(data=serializer_instance.data)

    def post(self,request):

        form_data=request.data

        serializer_instance=DoctorSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data=serializer_instance._validated_data

            Doctor.objects.create(**cleaned_data)

            return Response(data=serializer_instance.validated_data)

        else:

            return Response(serializer_instance.errors)

class DoctorRetrieveUpdataDeleteView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def get(self,request,pk=None):

        qs=Doctor.objects.get(id=pk)

        serializer_instance=DoctorSerializer(qs)

        return Response(data=serializer_instance.data)

    def put(self,request,pk=None):

        form_data=request.data

        serializer_instance=DoctorSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data=serializer_instance.validated_data

            Doctor.objects.filter(id=pk).update(**cleaned_data)

            return Response(data=serializer_instance.validated_data)

        else:

            return Response(data=serializer_instance.errors)

    def delete(self,request,pk=None):

        qs=Doctor.objects.get(id=pk).delete()

        serializer_instance=DoctorSerializer(qs)

class AdminCreateView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance._validated_data

            #User.objects.create(**cleaned_data)  -----here no encryption occurs , password just saved as plain text

            #User.objects.create_user(**cleaned_data) ----- here just user created, not adminuser

            User.objects.create_superuser(**cleaned_data)

            return Response(data=serializer_instance.validated_data)

        else:

            return Response(data=serializer_instance.errors)

        

