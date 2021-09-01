from rest_framework import viewsets

from FieldWorker.models import FieldWorker
from FieldWorker.serializers import FieldWorkerSerializer


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = FieldWorker.objects.all()
    serializer_class = FieldWorkerSerializer

    """
    def create(self, request):
        serializer = FieldWorkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        serializer = FieldWorkerSerializer(self.get_object(), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """
