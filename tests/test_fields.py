from django import forms
from django.test import TestCase
from django_aieditor.fields import AiEditorField, AiEditorModelField
from django.db import models


class TestForm(forms.Form):
    content = AiEditorField()


class TestModel(models.Model):
    content = AiEditorModelField()


class AiEditorFieldTests(TestCase):
    def test_form_field_rendering(self):
        form = TestForm()
        self.assertIn('class="aieditor"', str(form['content']))
        self.assertIn('aieditor.min.js', str(form.media))
        self.assertIn('aieditor.min.css', str(form.media))

    def test_model_field(self):
        field = TestModel._meta.get_field('content')
        self.assertIsInstance(field, AiEditorModelField)
        form_field = field.formfield()
        self.assertIsInstance(form_field, AiEditorField) 