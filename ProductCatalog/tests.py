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

    def find_id(self, id):
        return self.browser.find_element_by_id(id)

    def test_user_can_land(self):
        """
        Test that a user can visit the landing page and see the catalog.
        """

        # a list of catalog items should be visible

        home_page = self.browser.get(self.live_server_url + '/')

        # user should see some basic markup
        logo = self.find_id('logo')
        self.assertEqual('Product Catalog', logo.text)

        item_list = self.find_id('catalog-items')
        self.assertIsNotNone(item_list)

    def test_user_can_add_product(self):
        """
        Test that a user can:
            - navigate to the add product page
            - see the form for adding a product
            - add a product
            - be redirected to the product detail page
        """

        add_product_url = reverse('addproduct')
        self.browser.get('%s%s' % (self.live_server_url, add_product_url))
        self.assertIn('/product/add/', self.browser.current_url)

        add_product_form = self.find_id('product-form')
        self.assertIsNotNone(add_product_form)

        product_title_text = 'Add Product Test Product'
        self.find_id('id_name').send_keys(product_title_text)
        self.find_id('id_description').send_keys('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus enim ex, tincidunt a auctor nec, sodales sit amet massa.')
        self.find_id('id_width').send_keys('1.25')
        self.find_id('id_length').send_keys('3.45')
        self.find_id('id_height').send_keys('5.75')
        self.find_id('id_weight').send_keys('12.125')
        self.find_id('id_value').send_keys('49.95')

        self.browser.find_element_by_xpath('//input[@value="Add Product"]').click()

        product_title = self.browser.find_element_by_css_selector('h2')
        self.assertEqual(product_title_text, product_title.text)

    def tearDown(self):
        self.browser.quit()