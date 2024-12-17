from django import forms
from django.db import models
from django.conf import settings
from django.contrib.admin import widgets


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
                    'django_aieditor/css/style.css',
                )
            },
            js=(
                'django_aieditor/js/index.js',
                'django_aieditor/js/init.js',
            )
        )

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['config'] = getattr(settings, 'AIEDITOR_CONFIG', {})
        return context


class AiEditorAdminWidget(AiEditorWidget, widgets.AdminTextareaWidget):
    pass


class AiEditorField(forms.CharField):
    widget = AiEditorWidget

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AiEditorModelField(models.TextField):
    def formfield(self, **kwargs):
        if kwargs.get('widget') == widgets.AdminTextareaWidget:
            kwargs['widget'] = AiEditorAdminWidget
        else:
            kwargs['widget'] = AiEditorWidget
        return super().formfield(**kwargs) 