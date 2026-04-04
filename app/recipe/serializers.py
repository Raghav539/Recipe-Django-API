"""
Serializers for the recipe app.
"""
from rest_framework import serializers
from core.models import Recipe, Tag





class TagSerializer(serializers.ModelSerializer):
    """Serializer for recipe tags."""

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']

    def validate(self, attrs):
        request = self.context.get('request')
        if request and request.method == 'POST':
            if not attrs.get('name'):
                raise serializers.ValidationError('Name is required for creating a tag.')
        return attrs

class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe objects."""
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'description', 'link','tags']
        read_only_fields = ['id']

    def _get_or_create_tags(self, tags_data, recipe):
        """Handle getting or creating tags as needed."""
        auth_user = self.context['request'].user
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data, user=auth_user)
            recipe.tags.add(tag)

    def create(self, validated_data):
        """Create a recipe."""
        tags_data = validated_data.pop('tags', [])
        recipe = Recipe.objects.create(**validated_data)
        self._get_or_create_tags(tags_data, recipe)
        return recipe


    def update(self, instance, validated_data):
        """Update a recipe."""
        tags_data = validated_data.pop('tags', None)
        if tags_data is not None:

            instance.tags.clear()
            self._get_or_create_tags(tags_data, instance)


        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

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

