import json
import unittest

from northgate.models.site import Site


class TestSite(unittest.TestCase):
    def test_constructor_uses_expected_defaults(self):
        site = Site(name="Docs", visibility="public")

        self.assertEqual(site.name, "Docs")
        self.assertEqual(site.visibility, "public")
        self.assertFalse(site.local)
        self.assertIsNone(site.password)
        self.assertIsNone(site.entry)
        self.assertEqual(site.allowed_extensions, [])
        self.assertIsNone(site.description)

    def test_to_json_includes_all_site_fields(self):
        site = Site(
            name="Portal",
            visibility="private",
            local=True,
            password="secret",
            entry="index.html",
            allowed_extensions=[".html", ".css"],
            description="Internal portal",
        )

        self.assertEqual(
            json.loads(site.toJson()),
            {
                "name": "Portal",
                "visibility": "private",
                "local": True,
                "password": "secret",
                "entry": "index.html",
                "allowed_extensions": [".html", ".css"],
                "description": "Internal portal",
            },
        )

    def test_from_yaml_uses_defaults_for_optional_fields(self):
        site = Site.fromYaml({"name": "Blog", "visibility": "public"})

        self.assertEqual(site.name, "Blog")
        self.assertEqual(site.visibility, "public")
        self.assertFalse(site.local)
        self.assertIsNone(site.password)
        self.assertIsNone(site.entry)
        self.assertEqual(site.allowed_extensions, [])
        self.assertIsNone(site.description)

    def test_from_yaml_loads_yaml_string(self):
        site = Site.fromYaml(
            """
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

        self.assertEqual(site.name, "Example")
        self.assertEqual(site.visibility, "private")
        self.assertTrue(site.local)
        self.assertIsNone(site.password)
        self.assertEqual(site.entry, "index.html")
        self.assertEqual(site.allowed_extensions, [".html", ".css"])
        self.assertEqual(site.description, "Example site")


if __name__ == "__main__":
    unittest.main()