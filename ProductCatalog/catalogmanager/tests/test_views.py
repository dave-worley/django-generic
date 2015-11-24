from django.test import TestCase
from django.test import RequestFactory
from catalogmanager.views import index

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view_basic(self):
        """
        Just a simple index view test.
        """
        request = self.factory.get('/')
        with self.assertTemplateUsed('catalogmanager/index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)
