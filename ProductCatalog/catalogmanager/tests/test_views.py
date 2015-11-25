from django.contrib.staticfiles.testing import LiveServerTestCase
from django.test import RequestFactory
from django.db.models.query import QuerySet
from django.core.paginator import Page
from django.core.urlresolvers import reverse
from catalogmanager.views import index
from catalogmanager.views import productDetail

class IndexViewTestCase(LiveServerTestCase):

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
        Make sure we have some paginated Products in the response.
        """
        response = self.client.get('/')
        self.assertIs(type(response.context['products']), Page)


# class ProductDetailTestCase(LiveServerTestCase):
#
#     def test_detail_view_exists(self):
#         response = self.client.get('/product/1/')
#         self.assertEqual(response.status_code, 200)

class AddProductTestCase(LiveServerTestCase):

    def test_add_product_view_exists(self):
        response = self.client.get('/product/add/')
        self.assertEqual(response.status_code, 200)