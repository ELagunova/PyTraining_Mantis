from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            if field_name == "inherit_global_categories":
                if not text:
                    wd.find_element_by_type("checkbox").click()
            elif field_name == "status":
                wd.find_element_by_xpath("//select[@name='status']/option[text()='%s']" %text).click()
            elif field_name == "view_status":
                wd.find_element_by_xpath("//select[@name='view_state']/option[text()='%s']" %text).click()
            else:
                wd.find_element_by_name(field_name).send_keys(text)

    def fill_form(self, project):
        wd = self.app.wd
        self.change_field("name", project.name)
        self.change_field("status", project.status)
        self.change_field("view_status", project.view_status)
        self.change_field("description", project.description)

    def create(self, project):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def delete(self, project):
        wd = self.app.wd
        self.open_manage_project_page()
        wd.find_element_by_xpath("//a[text()='%s']" %project.name).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    def open_manage_project_page(self):
        wd = self.app.wd
        wd.get('http://localhost/mantisbt-1.2.20/manage_proj_page.php')

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_manage_project_page()
            self.project_cache = []
            rows = wd.find_elements_by_xpath("//table[@class='width100']//tr[starts-with(@class, 'row-')]")
            for element in rows[1:]:
                cells = element.find_elements_by_tag_name("td")
                name = cells[0].text
                status = cells[1].text
                view_status = cells[3].text
                description = cells[4].text
                self.project_cache.append(Project(name=name, status=status, view_status=view_status,
                                                  description=description))
        return self.project_cache
