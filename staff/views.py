from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import serializers

from staff.models import Doctor


# Create your views here.

class DoctorsListCreateView(APIView):

    def get(self,request):

        qs=Doctor.objects.all().values()

        doctors_list = list(qs)

        return Response(data=doctors_list)

    def post(self,request):

        form_data=request.data

        specialization=form_data.get("specialization")

        flat = [tp[0] for tp in Doctor.SPECIALIZATION_OPTIONS]

        if specialization not in flat:

            raise serializers.ValidationError(specialization," is not a valid choice .")

        fee = form_data.get("fee")

        if fee > 2000:

            raise serializers.ValidationError()


        Doctor.objects.all().create(**form_data)

        return Response({"message":"record added"})

class DoctorsRetrieveUpdateDeleteView(APIView):

    def get(self,request,pk=None):

        qs=Doctor.objects.filter(id=pk).values()

        doctor_list=list(qs)

        return Response(doctor_list)

    def put(self,request,pk=None):

        form_data=request.data

        qs=Doctor.objects.filter(id=pk).update(**form_data)

        return Response(data={"message":"updated..."})

    def delete(self,request,pk=None):

        Doctor.objects.get(id=pk).delete()

        return Response(data={"message":"record removed..."})


        



