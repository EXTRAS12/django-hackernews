from django.forms import ModelForm

from .models import Comment, Story


class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = (
            "title",
            "url",
            "text",
        )


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
