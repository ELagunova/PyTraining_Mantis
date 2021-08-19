from suds.client import Client
from suds import WebFault

from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.config["web"]["baseUrl"] + "api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_all_projects(self, username, password):
        client = Client(self.app.config["web"]["baseUrl"] + "api/soap/mantisconnect.php?wsdl")
        all_projects = []
        for project in client.service.mc_projects_get_user_accessible(username, password):
            all_projects.append(Project(id=project.id, name=project.name, status=project.status.name,
                                        view_status=project.view_state.name, description=project.description))
        return all_projects




