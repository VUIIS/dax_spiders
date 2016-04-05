import printutil
import xnat_utils2
from string import Formatter

# Mirror of the URIS here https://wiki.xnat.org/display/XNAT16/XNAT+REST+API+Directory

# User URIS
URI_USER_RESOURCE = '/data/user/cache/resources'
URI_USER_RESOURCES_BY_ID = '/data/user/cache/resources/{resource}'
URI_USER_FILE = '/data/user/cache/resources/{resource}/files'
URI_USER_FILE_BY_ID = '/data/user/cache/resources/{resource}/files/{file}'
URI_USER = '/data/users'
URI_USER_BY_ID = '/data/users/{user}'

# Project URIS
URI_PROJECT = '/data/archive/projects'
URI_PROJECT_BY_ID = '/data/archive/projects/{project}'
URI_PROJECT_ACCESSIBILITY = '/data/archive/projects/{project}/accessibility'
URI_PROJECT_ACCESSIBILITY_BY_TYPE = '/data/archive/projects/{project}/accessibility/{accessibility}'
URI_PROJECT_ARC_PATH = '/data/archive/projects/{project}/current_arc'
URI_PROJECT_ARC_PATH_BY_SUBDIR = '/data/archive/projects/{project}/current_arc/{folder}'
URI_PROJECT_FILES = '/data/archive/projects/{project}/files/{file}'
URI_PROJECT_PREARCHIVE_CODE = '/data/archive/projects/{project}/prearchive_code'
URI_PROJECT_PREARCHIVE_CODE_BY_ID = 'data/archive/projects/{project}/prearchive_code/{code}'
URI_PROJECT_QUARANTINE_CODE = '/data/archive/projects/{project}/quarantine_code'
URI_PROJECT_QUARANTINE_CODE_BY_ID = '/data/archive/projects/{project}/quarantine_code/{code}'
URI_PROJECT_RESOURCES = '/data/archive/projects/{project}/resources'
URI_PROJECT_RESOURCES_BY_ID = '/data/archive/projects/{project}/resources/{resource}'
URI_PROJECT_RESOURCES_BY_FILENAME = '/data/archive/projects/{project}/resources/{resource}/files/{file}'
URI_PROJECT_SEARCHES = '/data/archive/projects/{project}/searches/{search}'

# Session URIS
URI_SESSION_ASSESSOR = '/data/archive/projects/{project}/subjects/{subject_label}/experiments/{session_label}/assessors'
URI_SESSION_ASSESSOR_BY_ID = '/data/archive/projects/{project}/subjects/{subject_label}/experiments/{session_label}/assessors/{assessor_label}'
URI_SESSION_ASSESSOR_FILE_BY_ID = '/data/archive/projects/{project}/subjects/{subject_label}/experiments/{session_label}/assessors/{assessor_label}/out/files/{file}'
URI_SESSION_ASSESSOR_RESOURCE = '/data/archive/projects/{project}/subjects/{subject_label}/experiments/{session_label}/assessors/{assessor_label}/out/resources'
URI_SESSION_ASSESSOR_RESOURCE_BY_ID = '/data/archive/projects/{project}/subjects/{subject_label}/experiments/{session_label}/assessors/{assessor_label}/out/resources/{resource}'
URI_SESSION_ASSESSOR_RESOURCE_FILE_BY_ID = '/data/archive/projects/{project}/subjects/{subject_label}/experiments/{session_label}/assessors/{assessor_label}/out/resources/{resource}/files/{file}'
URI_SESSION_SCAN = '/data/archive/projects/{project}/subjects/{subject_label}/experiments/{session_label}/scans'
URI_SESSION_SCAN_BY_ID = '/data/archive/projects/{project}/subjects/{subject_label}/experiments/{session_label}/scans/{scan_id}'
URI_SESSION_SCAN_FILE_BY_ID = '/data/archive/projects/{project}/subjects/{subject_label}/experiments/{session_label}/scans/{scan_id}/files/{file}'
URI_SESSION_SCAN_RESOURCE = '/data/archive/projects/{project}/subjects/{subject_label}/experiments/{session_label}/scans/{scan_id}/resources'
URI_SESSION_SCAN_RESOURCE_BY_ID = '/data/archive/projects/{project}/subjects/{subject_label}/experiments/{session_label}/scans/{scan_id}/resources/{resource}'
URI_SESSION_SCAN_RESOURCE_FILE_BY_ID = '/data/archive/projects/{project}/subjects/{subject_label}/experiments/{session_label}/scans/{scan_id}/resources/{resource}/files/{file}'

# Prearchive URIS
URI_PREARCHIVE_PROJECT = '/data/prearchive/projects'
URI_PREARCHIVE_PROJECT_BY_ID = '/data/prearchive/projects/{project}'
URI_PREARCHIVE_SESSION_BY_ID = '/data/prearchive/projects/{project}/{timestamp}/{session_label}'
URI_PREARCHIVE_SCAN = '/data/prearchive/projects/{project}/{timestamp}/{session_label}/scans'
URI_PREARCHIVE_SCAN_BY_ID = '/data/prearchive/projects/{project}/{timestamp}/{session_label}/scans/{scan_id}/resources'
URI_PREARCHIVE_SCAN_FILE = '/data/prearchive/projects/{project}/{timestamp}/{session_label}/scans/{scan_id}/resources/{resource}/files'
URI_PREARCHIVE_SCAN_FILE_BY_ID = '/data/prearchive/projects/{project}/{timestamp}/{session_label}/scans/{scan_id}/resources/{resource}/files/{file}'

# Archive URIS
URI_ARCHIVE_SESSION_BY_ID = '/data/archive/experiments/{session_label}'
URI_ARCHIVE_ASSESSOR_BY_ID = '/data/archive/experiments/{session_label}/assessors/{ID}'
URI_ARCHIVE_SCAN_BY_ID = '/data/archive/experiments/{session_label}/scans/{ID}'
URI_ARCHIVE_PROJECT_BY_ID = '/data/archive/projects/{project}'
URI_ARCHIVE_SUBJECT_BY_ID = '/data/archive/projects/{project}/subjects/{subject_label}'
URI_ARCHIVE_SESSION_BY_ID = '/data/archive/projects/{project}/subjects/{subject_label}/experiments/{session_label}'
URI_ARCHIVE_ASSESSOR = '/data/archive/projects/{project}/subjects/{subject_label}/experiments/{session_label}/assessors'
URI_ARCHIVE_SUJECT_ID_AND_SCAN_ID = '/data/archive/projects/{project}/subjects/{subject_label}/experiments/{session_label}/scans/{scan_id}'

# Service URIS
URI_SERVICE_ARCHIVE = '/data/services/archive'
URI_SERVICE_DCMSCP = '/data/services/dicomscp'
URI_SERVICE_IMPORT = '/data/services/import'
URI_SERVICE_PREARCHIVE_DELETE = '/data/services/prearchive/delete'
URI_SERVICE_PREARCHIVE_MOVE ='/data/services/prearchive/move'
URI_SERVICE_REFRESH_CATALOG = '/data/services/refresh/catalog'
URI_SERVICE_VALIDATE_ARCHIVE = '/data/services/validate-archive'
URI_SERVICE_STATUS_BY_ID = '/data/status/{status}'
URI_SERVICE_VERSION = '/data/version'


class XNATURI(object):

    def __init__(self, xnat, uri, value_dict):
        self.xnat = xnat
        self.uri = uri
        self.value_dict = value_dict
        self.uri_obj = None

    def format_uri(self):
        '''
        Method to format any URI given a dict of key value pairs

        :param uri: String template of a URI
        :param value_dict: key value pairs where the keys are in the URI and the
         values are the value to insert
        :return: Formatted URI with text inserted

        '''

        uri_out = None
        try:
            uri_out = self.uri.format(**self.value_dict)
        except KeyError as KE:
            printutil.print_warning_message(KE.message)
        return uri_out

    def exists(self):
        '''
        Method that calls the pyxnat "exists()" method

        :return: True/False if object exists

        '''

        if self.uri_obj is None:
            return False
        else:
            return self.uri_obj.exists()

    def select(self):
        '''
        Calls a wrapper method for pyxnat's select method

        :return: None
        '''
        self.uri_obj = xnat_utils2.wrapped_select(self.xnat, self.uri)

    def delete(self):
        '''
        Calls a wrapper method for pyxnats delete method

        :return: None
        '''

        if self.uri_obj.exits():
            xnat_utils2.wrapped_delete(self.uri_obj)

    def get_keys(self):
        '''
        Method to return the keys in the URI

        :return: list of keys in URI
        '''

        return [i[1] for i in Formatter().parse(self.uri)]

