from django.test import TestCase
from django.test import RequestFactory
from django.db.models.query import QuerySet
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

    def test_index_view_returns_products(self):
        """
        Make sure we have some Products in the response.
        """
        response = self.client.get('/')
        self.assertIs(type(response.context['products']), QuerySet)
