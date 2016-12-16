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

Add the following to your root `urls.py` file:
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

Add the following to your root `urls.py` file:
```
urlpatterns = [
    ...
    url(r'^dev/', include('dev.urls')),
]
```


# Development console usage

## Sequencing genetic file retrieval

![Sequencing genetic file retrieval](doc/resources/Screenshot%20from%202016-12-16%2018-12-30.png?raw=true)

##### Specify Sequencing genetic file retrieval endpoint URI: 

![URI](doc/resources/file-retrieval-url.png?raw=true)

##### Specify token provided by Sequencing on the authorization phase:

![Sequencing authentication token](doc/resources/sequencing-auth-token.png?raw=true)

##### Specify file Id that needs to be retrieval:

![File ID](doc/resources/file-id.png?raw=true)

##### Testing

Click `Test` button to send request.

After sending request, fields `Request` and `Response` will contain appropriate request and Sequencing response details:

![File retrieval test](doc/resources/file-retrieval-test.png?raw=true)


## Sequencing job status notification 

![Sequencing job status notification](doc/resources/job-status-notification-endpoint.png?raw=true)

##### Specify Sequencing job status notification endpoint URI:

![Sequencing authentication token](doc/resources/sequencing-auth-token.png?raw=true)


##### Specify Sequencing job identifier:

![Sequencing job identifier](doc/resources/sequencing-job-id.png?raw=true)

##### Specify job processing status:

![processing status](doc/resources/processing_status.png?raw=true)

You can choose one of:

![processing status choose](doc/resources/processing_status_choose.png?raw=true)

##### Specify completion status:

![completion status](doc/resources/completion_status.png?raw=true)

You can choose one of:

![completion status choose](doc/resources/completion_status_choose.png?raw=true)

##### Specify error message:

If processing completed with error, you can specify error details:

![error message](doc/resources/error_message.png?raw=true)


##### Specify output files:

There is no limitation on content returned by this URL.
This URL should be directly accessible without need to perform authentication.

![output files](doc/resources/otuput-files.png?raw=true)

You can add more files as needed, for this click `+` button in `Output files` section:

![output files add](doc/resources/output-files-new.png?raw=true)


##### Specify additional specific attributes that needs to be transferred to 3rd party:

![additional attributes](doc/resources/additional-attr.png?raw=true)

You can add more attributes as needed, for this click `+` button in `Additional specific attributes that needs to be transferred to 3rd party` section:

![additional attributes add](doc/resources/additional-attr-new.png?raw=true)


##### Specify callback details:

Credentials specified in `username` and `password` fields will be used by the user to access results available by the link specified by `url` link.

![callback](doc/resources/callback.png?raw=true)


##### Testing

Click `Test` button to send request.

After sending request, fields `Request` and `Response` will contain appropriate request and Sequencing response details:

![job status notification test](doc/resources/job-status-notification-test.png?raw=true)
