import json
import unittest
from uuid import uuid8

from northgate.models.site import Site


class TestSite(unittest.TestCase):
    def test_constructor_uses_expected_defaults(self):
        id = uuid8()
        site = Site(id=id, name="Docs", visibility="public", path="/sites/local")

        self.assertEqual(site.name, "Docs")
        self.assertEqual(site.visibility, "public")
        self.assertEqual(site.path, "/sites/local")
        self.assertFalse(site.local)
        self.assertIsNone(site.password)
        self.assertIsNone(site.entry)
        self.assertEqual(site.allowed_extensions, [])
        self.assertIsNone(site.description)

    def test_to_json_includes_all_site_fields(self):
        id = uuid8()
        site = Site(
            id=str(id),
            name="Portal",
            visibility="private",
            path="/sites/portal",
            local=True,
            password="secret",
            entry="index.html",
            allowed_extensions=[".html", ".css"],
            description="Internal portal",
        )

        self.assertEqual(
            json.loads(site.toJson()),
            {
                "id": str(id),
                "name": "Portal",
                "visibility": "private",
                "path": "/sites/portal",
                "local": True,
                "password": "secret",
                "entry": "index.html",
                "allowed_extensions": [".html", ".css"],
                "description": "Internal portal",
            },
        )

    def test_from_yaml_uses_defaults_for_optional_fields(self):
        id = uuid8()
        site = Site.fromYaml(id=id, path="/sites/blog", yaml_data={"name": "Blog", "visibility": "public"})

        self.assertEqual(site.id, id)
        self.assertEqual(site.name, "Blog")
        self.assertEqual(site.visibility, "public")
        self.assertEqual(site.path, "/sites/blog")
        self.assertFalse(site.local)
        self.assertIsNone(site.password)
        self.assertIsNone(site.entry)
        self.assertEqual(site.allowed_extensions, [])
        self.assertIsNone(site.description)

    def test_from_yaml_loads_yaml_string(self):
        id = uuid8()
        site = Site.fromYaml(id=id, path="/sites/example", yaml_data="""
            name: Example
            visibility: private
            local: true
            password: null
            entry: index.html
            allowed_extensions:
              - .html
              - .css
            description: Example site
            """
        )

        self.assertEqual(site.id, id)
        self.assertEqual(site.name, "Example")
        self.assertEqual(site.visibility, "private")
        self.assertEqual(site.path, "/sites/example")
        self.assertTrue(site.local)
        self.assertIsNone(site.password)
        self.assertEqual(site.entry, "index.html")
        self.assertEqual(site.allowed_extensions, [".html", ".css"])
        self.assertEqual(site.description, "Example site")


if __name__ == "__main__":
    unittest.main()