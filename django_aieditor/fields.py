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
                    'django_aieditor/css/aieditor.min.css',
                )
            },
            js=(
                'django_aieditor/js/aieditor.umd.js',
                'django_aieditor/js/init.js',
            )
        )

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        # 获取默认配置
        default_config = {
            'minHeight': '400px',  # 最小高度
            'maxHeight': '800px',  # 最大高度
            'placeholder': '请输入内容...',  # 占位提示文本
            'mode': 'simple',  # 使用简单模式
            'toolbarKeys': [
                'bold', 'italic', 'strikethrough', 'underline', 'code', '|',
                'heading', 'quote', 'unorderedList', 'orderedList', 'todoList', '|',
                'link', 'image', 'table', '|',
                'preview', 'fullscreen'
            ],
            'upload': {
                'url': '/upload/',
                'headers': {
                    'X-CSRFToken': '{{ csrf_token }}'
                }
            }
        }

        # 获取用户配置
        user_config = getattr(settings, 'AIEDITOR_CONFIG', {})
        
        # 递归合并配置
        def merge_config(default, user):
            result = default.copy()
            for key, value in user.items():
                if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                    result[key] = merge_config(result[key], value)
                else:
                    result[key] = value
            return result

        # 合并配置
        final_config = merge_config(default_config, user_config)
        context['widget']['config'] = final_config
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