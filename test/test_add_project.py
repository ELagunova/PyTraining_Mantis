import string
import random
import pytest

from model.project import Project


def random_string(prefix='', maxlen=1, postfix=''):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + postfix


@pytest.mark.parametrize('status, view_status',
                         [('release', 'public'), ('development', 'private'),
                          ('stable', 'private'), ('obsolete', 'public')])
def test_add_project(app, config, status, view_status):
    project = Project(name=random_string('test', 5), status=status, view_status=view_status,
                      description=random_string(maxlen=5))
    username = config["webadmin"]["username"]
    password = config["webadmin"]["password"]
    old_projects = app.soap.get_all_projects(username, password)
    app.project.create(project)
    new_projects = app.soap.get_all_projects(username, password)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


