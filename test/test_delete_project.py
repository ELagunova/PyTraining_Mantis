import random


def test_delete_project(app):
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete(project)
    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    assert old_projects == new_projects


