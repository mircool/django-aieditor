from setuptools import setup, find_packages
import io

with io.open("README.md", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="django-aieditor",
    version="0.1.4",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    description="Django-AiEditor 是一个为 Django 框架提供的 AiEditor 富文本编辑器集成包。",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mircool/django-aieditor",
    author="mircool",
    author_email="mircool@qq.com",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=[
        "Django>=3.2",
    ],
    python_requires=">=3.7",
) 