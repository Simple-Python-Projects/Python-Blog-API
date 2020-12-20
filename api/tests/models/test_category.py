from django.test import TestCase
from api.models.category import Category


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="Foo", slug="foo")
        Category.objects.create(name="Bar", slug="bar")

    def test_category_names(self):
        foo = Category.objects.get(id=1)
        bar = Category.objects.get(id=2)

        self.assertEqual(foo.slug, 'foo')
        self.assertEqual(foo.name, 'Foo')

        self.assertEqual(bar.slug, 'bar')
        self.assertEqual(bar.name, 'Bar')
