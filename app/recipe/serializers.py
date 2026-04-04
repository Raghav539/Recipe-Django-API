"""
Serializers for the recipe app.
"""
from rest_framework import serializers
from core.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe objects."""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'description', 'link']
        read_only_fields = ['id']

    def validate(self,attrs):
        request = self.context.get('request')
        if request and request.method == 'POST':
            if not attrs.get('title'):
                raise serializers.ValidationError('Title is required for creating a recipe.')
        return attrs


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view."""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']