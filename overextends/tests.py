
from __future__ import with_statement
import os
from shutil import rmtree
import sys
from uuid import uuid4

from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from django.test import TestCase


TEST_TEMPLATE = """

{# avast ye mateys #}
%(extends_string)s
{%% block main %%}
%(super_string)s
%(test_string)s
{%% endblock %%}

"""


class Tests(TestCase):
    """
    Test that ``overextends`` triggers across multiple project and
    app templates with the same relative path. To achieve this, we
    need the same template name to exist in multiple apps, as well as
    at the project level, so we create some fake apps and a project
    template. These all used a unique ID to ensure they don't
    collide with anything in the project. When we're done, we clean
    up our mess.
    """

    def setUp(self):
        """
        Put the test template into a couple of test apps and the project.
        """

        self.root = os.path.dirname(__import__(settings.ROOT_URLCONF).__file__)
        sys.path.append(self.root)

        # Add the test apps to INSTALLED_APPS.
        self.unique_id = str(uuid4()).replace("-", "")
        self.test_apps = ["app%s%s" % (i, self.unique_id) for i in range(10)]

        # Create the app directories with the test template.
        for test_app in self.test_apps:
            app_dir = os.path.join(self.root, test_app)
            os.mkdir(app_dir)
            app_templates = os.path.join(app_dir, "templates")
            os.mkdir(app_templates)
            with open(os.path.join(app_dir, "__init__.py"), "w") as f:
                f.write("")
            extends = test_app != self.test_apps[-1]
            self._create_template(app_templates, test_app, extends)

        # Add the test template to the project, and store a flag
        # indicating whether or not the project templates directory
        # existed, so if it does, we can leave it in place when we
        # clean everything up.
        project_templates = os.path.join(self.root, "templates")
        self.project_templates_exist = os.path.exists(project_templates)
        if not self.project_templates_exist:
            os.mkdir(project_templates)
        self._create_template(project_templates, "project", True)

    def _create_template(self, template_dir, test_string, extends):
        """
        Creates the test template in the given template directory, with
        the test string injected that we'll use for the real test.
        """
        with open(os.path.join(template_dir, self.unique_id), "w") as f:
            template_vars = {
                "test_string": test_string,
                "extends_string": "",
                "super_string": "",
            }
            if extends:
                extends_string = "{%% overextends \"%s\" %%}" % self.unique_id
                template_vars["extends_string"] = extends_string
                template_vars["super_string"] = "{{ block.super }}"
            f.write((TEST_TEMPLATE % template_vars).strip())

    def test_overextends(self):
        """
        Ensure the test string appear in the rendered template.
        """
        with self.modify_settings(INSTALLED_APPS={
                    'prepend': self.test_apps
                }):
            html = get_template(self.unique_id).render({})
            previous = ""
            for test_string in ["project"] + self.test_apps:
                self.assertTrue(test_string in html)
                if previous:
                    self.assertTrue(html.index(test_string) < html.index(previous))
                previous = test_string

    def tearDown(self):
        """
        Delete all the temp files and directories we created in ``setUp``.
        """
        for test_app in self.test_apps:
            rmtree(os.path.join(self.root, test_app))
        if self.project_templates_exist:
            os.remove(os.path.join(self.root, "templates", self.unique_id))
        else:
            rmtree(os.path.join(self.root, "templates"))
