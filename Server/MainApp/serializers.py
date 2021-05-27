from rest_framework import serializers
from .models import *


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = ('player', 'score')

    def create(self, validated_data):
        model = Records(
            player=validated_data['player'],
            score=validated_data['score'],
        )
        model.save()
        return model
