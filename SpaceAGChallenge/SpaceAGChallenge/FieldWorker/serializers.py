import re

from rest_framework import serializers

from FieldWorker.models import FieldWorker


class FieldWorkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FieldWorker
        fields = ['id', 'first_name', 'last_name', 'function', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_first_name(self, value):
        value = re.sub('[^A-Za-z0-9 ]+', '', value.strip())
        if value is None or value == "":
            raise serializers.ValidationError("first_name cannot be null")

        return value

    def validate_last_name(self, value):
        value = re.sub('[^A-Za-z0-9 ]+', '', value.strip())
        if value is None or value == "":
            raise serializers.ValidationError("last_name cannot be null")

        return value

    def validate_function(self, value):
        value = value.strip()
        if value.upper() != 'HARVEST' and value.upper() != 'PRUNNING' and value.upper() != 'SCOUTING' and value.upper() != 'OTHER':
            value = 'Other'

        return value
