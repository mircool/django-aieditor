from django import forms
from django.db import models
from django.conf import settings


class AiEditorWidget(forms.Textarea):
    template_name = 'django_aieditor/widget.html'

    def __init__(self, attrs=None):
        default_attrs = {'class': 'aieditor'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)

    @property
    def media(self):
        return forms.Media(
            css={
                'all': (
                    'django_aieditor/css/aieditor.min.css',
                )
            },
            js=(
                'django_aieditor/js/aieditor.min.js',
                'django_aieditor/js/init.js',
            )
        )

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['config'] = getattr(settings, 'AIEDITOR_CONFIG', {})
        return context


class AiEditorField(forms.CharField):
    widget = AiEditorWidget

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AiEditorModelField(models.TextField):
    def formfield(self, **kwargs):
        defaults = {'form_class': AiEditorField}
        defaults.update(kwargs)
        return super().formfield(**defaults) 