from datetime import datetime

from django.test import TestCase
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from api.models import Tag
from api.serializers import TagSerializer


class TagSerializerTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(name="Foo", slug="foo-slug")

    def test_all_tags(self):
        tags = Tag.objects.all()
        tag_serializer = TagSerializer(tags[0])
        self.assertEqual(tag_serializer.data['id'], 1)
        self.assertEqual(tag_serializer.data['name'], "Foo")
        self.assertEqual(tag_serializer.data['slug'], "foo-slug")
        self.assertLess(datetime.strptime(tag_serializer.data['createdAt'], '%Y-%m-%dT%H:%M:%S.%fZ'), datetime.now())

