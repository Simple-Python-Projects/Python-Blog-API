from django.test import TestCase
from api.models.tag import Tag


class TagTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(name="Foo", slug="foo")
        Tag.objects.create(name="Bar", slug="bar")

    def test_tag_names(self):
        foo = Tag.objects.get(id=1)
        bar = Tag.objects.get(id=2)

        self.assertEqual(foo.slug, 'foo')
        self.assertEqual(foo.name, 'Foo')

        self.assertEqual(bar.slug, 'bar')
        self.assertEqual(bar.name, 'Bar')
