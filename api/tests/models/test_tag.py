from django.test import TestCase
from api.models.tag import Tag


class TagTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(name="Foo")
        Tag.objects.create(name="Bar")

    def test_tag_names(self):
        foo = Tag.objects.get(id=1)
        bar = Tag.objects.get(id=2)
        self.assertEqual(foo.name, 'Foo')
        self.assertEqual(bar.name, 'Bar')
