# Django-AiEditor

Django-AiEditor 是一个为 Django 框架提供的 AiEditor 富文本编辑器集成包。AiEditor 是一个强大的 Web 富文本编辑器。

## 安装

```bash
pip install django-aieditor
```

## 快速开始

1. 将 'django_aieditor' 添加到你的 INSTALLED_APPS 中：

```python
INSTALLED_APPS = [
    ...
    'django_aieditor',
]
```

2. 在你的模板中使用：

```html
{% load django_aieditor %}

<form method="post">
    {% csrf_token %}
    {{ form.media }}
    {% aieditor "content" %}
    <button type="submit">提交</button>
</form>
```

3. 在你的表单中：

```python
from django_aieditor.fields import AiEditorField

class MyForm(forms.Form):
    content = AiEditorField()
```

## 配置

在你的 settings.py 中可以添加以下配置：

```python
AIEDITOR_CONFIG = {
    'height': '400px',
    'width': '100%',
    'toolbar': ['bold', 'italic', 'link', 'image'],
    'upload_url': '/upload/',  # 文件上传接口
}
```

## 特性

- 完整支持 AiEditor 的所有功能
- 简单的 Django 集成
- 支持文件上传
- 支持自定义配置
- Django Admin 集成

## 文档

完整文档请访问：[https://github.com/mircool/django-aieditor](https://github.com/mircool/django-aieditor)

## License

MIT License 