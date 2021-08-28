from FieldWorker.models import FieldWorker
from rest_framework import serializers


class FieldWorkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FieldWorker
        fields = ['id', 'first_name', 'last_name', 'function', 'created_at']