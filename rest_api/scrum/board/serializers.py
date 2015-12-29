from rest_framework import serializers

from .models import Sprint


class SprintSerlializer(serializers.ModelSerializer):

	class Meta:
		model = Sprint
		fields = ('id', 'name', 'description', 'end', )