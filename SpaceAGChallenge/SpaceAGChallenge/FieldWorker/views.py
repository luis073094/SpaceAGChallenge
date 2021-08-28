from django.shortcuts import render
from FieldWorker.models import FieldWorker
from rest_framework import viewsets
from FieldWorker.serializers import FieldWorkerSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = FieldWorker.objects.all()
    serializer_class = FieldWorkerSerializer

    def create(self, request):
        function = request.data['function']
        function = function.strip()

        if function.upper() != 'HARVEST' and function.upper() != 'PRUNNING' and function.upper() != 'SCOUTING' and function.upper() != 'OTHER':
            function = 'Other'

        worker = FieldWorker.objects.create(
            first_name = request.data['first_name'].strip(),
            last_name = request.data['last_name'].strip(),
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

        worker.first_name = request.data.get('first_name', worker.first_name)
        worker.last_name = request.data.get('last_name', worker.last_name)
        worker.function = function
        worker.save()

        serializer = self.get_serializer(worker)
        return Response(serializer.data)
