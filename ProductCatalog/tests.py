from django.test import LiveServerTestCase
from django.core.urlresolvers import reverse
from selenium import webdriver
from catalogmanager.models import Product

class CatalogUserTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

        Product.objects.create(
            name='Test Product',
            description='This is a test product description.',
            width=12.75,
            length=24.25,
            height=32,
            weight=125,
            value=59.95
        )

    def test_user_can_land(self):
        """
        Test that a user can visit the landing page and see the catalog.
        """

        # a list of catalog items should be visible

        home_page = self.browser.get(self.live_server_url + '/')

        # user should see some basic markup
        logo = self.browser.find_element_by_id('logo')
        self.assertEqual('Product Catalog', logo.text)

        item_list = self.browser.find_element_by_id('catalog-items')
        self.assertIsNotNone(item_list)

    def test_user_can_visit_add_product(self):
        """
        Test that a user can:
            - navigate to the add product page
            - see the form for adding a product
            - add a product
            - be redirected to the product detail page
        """

        add_product_url = reverse('addproduct')
        add_product_page = self.browser.get('%s%s' % (self.live_server_url, add_product_url))
        self.assertIn('/product/add/', self.browser.current_url)

    def tearDown(self):
        self.browser.quit()