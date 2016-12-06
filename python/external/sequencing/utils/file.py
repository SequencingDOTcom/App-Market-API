import os
import errno
import urllib2

from external.sequencing.config import SequencingEndpoints


def retrieve_file(data_file_id, sequencing_token, uri=SequencingEndpoints.file_retrieval):
    """
    :param data_file_id: Sequencing data file id
    :param sequencing_token: Sequencing auth token
    :param uri: File retrieval endpoint
    :return: HTTP request and response
    """
    url = "{0}?id={1}".format(uri, data_file_id)

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'application/octet-stream',
        'Authorization': 'Bearer %s' % sequencing_token
    }

    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)

    return request, response


def create_dir(path):
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    return path
