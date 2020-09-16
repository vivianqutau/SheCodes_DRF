from rest_framework import serializers
from .models import Project, Pledge

class PledgeSerializer(serializers.Serializer):
    id=serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    supporter_id = serializers.IntegerField()
    project_id = serializers.IntegerField()

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    date_updated = serializers.DateTimeField()
    owner =serializers.ReadOnlyField(source='owner.id')
    # owner = serializers.CharField(max_length=200)
    # pledges = PledgeSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open =validated_data.get('is_open', instance.is_open)
        instance.date_updated =validated_data.get('date_updated', instance.date_updated)
        instance.save()
        return instance