from rest_framework import serializers

from app.models.todo import Todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    """
    A todo serializer.
    """
    # items = serializers.HyperlinkedRelatedField(many=True, view_name="item-detail", read_only=True)
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Todo
        fields = ("url", "id", "owner", "title", "created", "modified")
