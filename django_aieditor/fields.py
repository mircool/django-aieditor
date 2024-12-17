from django import forms
from django.db import models
from django.conf import settings
from django.contrib.admin import widgets
import json


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
                    'https://unpkg.com/aieditor@latest/dist/style.css',
                )
            },
            js=(
                'https://unpkg.com/aieditor@latest/dist/index.js',
            )
        )

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        # 获取默认配置
        default_config = {
            'height': '400px',
            'width': '100%',
            'mode': 'simple',  # 使用简单模式
            'toolbar': [
                'bold', 'italic', 'strikethrough', 'underline', 'code', '|',
                'heading', 'quote', 'unorderedList', 'orderedList', 'todoList', '|',
                'link', 'image', 'table', '|',
                'preview', 'fullscreen'
            ]
        }
        # 合并用户配置
        user_config = getattr(settings, 'AIEDITOR_CONFIG', {})
        default_config.update(user_config)
        context['widget']['config'] = default_config
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