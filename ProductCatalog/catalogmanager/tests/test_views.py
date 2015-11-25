from django.contrib.staticfiles.testing import LiveServerTestCase
from django.test import RequestFactory
from django.db.models.query import QuerySet
from django.core.paginator import Page
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

class ProductViewTestCase(LiveServerTestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_product_view_basic(self):
        """
        Makes sure the product detail view exists and uses the correct template.
        """
        request = self.factory.get('/product/1/')
        self.assertTemplateUsed('catalogmanager/product.html')