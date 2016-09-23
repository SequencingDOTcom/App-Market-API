import os
import errno
import wget

from external.sequencing.config import SequencingEndpoints


def download(data_file_id, sequencing_token, path):
    """
    :param data_file_id: Sequencing data file id
    :param sequencing_token: Sequencing auth token
    :param path: Output parent directory or full path
    :return: Full path to downloaded file
    """
    url = "{0}?id={1}&apiKey={2}".format(SequencingEndpoints.file_retrieval, data_file_id, sequencing_token)
    return wget.download(url, create_dir(path), bar=None)


def create_dir(path):
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    return path
