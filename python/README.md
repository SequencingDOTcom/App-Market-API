# Drop-in bootstrap integration

## Requirements

* Python 2.7
* Django 1.8

## Installation

#### Installing django rest framework

Install using `pip`:
```
pip install djangorestframework
```

Add `'rest_framework'` and `'rest_framework.authtoken'` to your `INSTALLED_APPS` setting:
```
INSTALLED_APPS = (
    ...
    'rest_framework',
    'rest_framework.authtoken',
)
```

#### Cloning drop-in bootstrap repository

Clone using `git`:
```
cd /tmp
git clone https://github.com/SequencingDOTcom/App-Market-API-integration.git
```

#### Installing *external* application

Deploy application:
```
cp -r /tmp/App-Market-API-integration/python/external <your_project_location>/external
```

Add `'external'` to your `INSTALLED_APPS` setting:
```
INSTALLED_APPS = (
    ...
    'external',
)
```

Add the following to your root *urls.py* file:
```
urlpatterns = [
    ...
    url(r'^external/', include('external.urls')),
]
```

#### Installing *development console* application

Deploy application:
```
cp -r /tmp/App-Market-API-integration/python/dev <your_project_location>/dev
```

Add `'dev'` to your `INSTALLED_APPS` setting:
```
INSTALLED_APPS = (
    ...
    'dev',
)
```

Add the following to your root *urls.py* file:
```
urlpatterns = [
    ...
    url(r'^dev/', include('dev.urls')),
]
```
