from django.shortcuts import render
from FieldWorker.models import FieldWorker
from rest_framework import viewsets
from FieldWorker.serializers import FieldWorkerSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
import re
from rest_framework.exceptions import APIException

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = FieldWorker.objects.all()
    serializer_class = FieldWorkerSerializer

    def create(self, request):
        function = request.data['function']
        function = function.strip()

        if function.upper() != 'HARVEST' and function.upper() != 'PRUNNING' and function.upper() != 'SCOUTING' and function.upper() != 'OTHER':
            function = 'Other'

        vfirst_name = re.sub('[^A-Za-z0-9 ]+', '', request.data['first_name'].strip())
        if vfirst_name is None or vfirst_name == "":
            raise APIException("first_name cannot be null")

        vlast_name = re.sub('[^A-Za-z0-9 ]+', '', request.data['last_name'].strip())
        if vlast_name is None or vlast_name == "":
            raise APIException("last_name cannot be null")
        

        worker = FieldWorker.objects.create(
            first_name = vfirst_name,
            last_name = vlast_name,
            function = function
        )
        serializer = self.get_serializer(worker)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        worker = self.get_object()

        function = request.data.get('function', worker.function)
        function = function.strip()

        if function.upper() != 'HARVEST' and function.upper() != 'PRUNNING' and function.upper() != 'SCOUTING' and function.upper() != 'OTHER':
            function = 'Other'

        vfirst_name = re.sub('[^A-Za-z0-9 ]+', '', request.data.get('first_name', worker.first_name))
        if vfirst_name is None or vfirst_name == "":
            raise APIException("first_name cannot be null")

        vlast_name = re.sub('[^A-Za-z0-9 ]+', '', request.data.get('last_name', worker.last_name))
        if vlast_name is None or vlast_name == "":
            raise APIException("last_name cannot be null")

        worker.first_name = vfirst_name
        worker.last_name = vlast_name
        worker.function = function
        worker.save()

        serializer = self.get_serializer(worker)
        return Response(serializer.data)
