__author__ = 'ptesser'
from asana import asana


class MyAPI:

    __asana_api = asana

    def __init__(self):
        self.__asana_api = asana.AsanaAPI('6muBM1Ce.T7a9CNPAjqLScdNgknQOdL6', debug=True)

    def get_id_workspace(self, project_name):
        myspaces = self.__asana_api.list_workspaces()
        for space in myspaces:
            if space['name'] == project_name:
                return space['id']

    def get_id_tag(self, workspace_id, tag_name):
        my_tags = self.__asana_api.get_tags(workspace_id)
        for tag in my_tags:
            if tag['name'] == tag_name:
                return tag['id']

    def get_asana_api(self):
        return self.__asana_api