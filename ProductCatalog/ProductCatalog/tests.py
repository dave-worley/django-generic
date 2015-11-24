from django.test import LiveServerTestCase
from selenium import webdriver

class CatalogUserTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def test_user_can_land(self):
        """
        Test that a user can visit the landing page and see the catalog.
        """

        # user may or may not be registered
        # a list of catalog items should be visible

        home_page = self.browser.get(self.live_server_url + '/')

        # user should see some basic markup
        logo = self.browser.find_element_by_id('logo')
        self.assertEqual('Product Catalog', logo.text)

        item_list = self.browser.find_element_by_id('catalog-items')
        self.assertIsNotNone(item_list)

        add_product_button = self.browser.find_element_by_id('add-product')
        self.assertEqual('Add Product', add_product_button.text)

        self.fail('Incomplete test.')

    def tearDown(self):
        self.browser.quit()
