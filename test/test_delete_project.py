import random

from model.project import Project


def test_delete_project(app, config):
    username = config["webadmin"]["username"]
    password = config["webadmin"]["password"]
    old_projects = app.soap.get_all_projects(username, password)
    project = random.choice(old_projects)
    app.project.delete(project)
    new_projects = app.soap.get_all_projects(username, password)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


