import pytest
from pom.pages.products_page import ProductsPage
from pom.pages.navigation_page import NavigationPage


@pytest.mark.usefixtures("set_up")
@pytest.mark.usefixtures("log_in")
class TestCompareProducts:

    def test_product_compare(self):
        navigation_page = NavigationPage(self.driver)
        products_page = ProductsPage(self.driver)
        navigation_page.open_gear_bags()
        products_page.select_product(0)
        products_page.click_add_to_compare()
        message = products_page.get_compare_success_message()
        assert message == "You added product Push It Messenger Bag to the comparison list."

    def test_sort_by_price_and_add_to_compare(self):
        navigation_page = NavigationPage(self.driver)
        products_page = ProductsPage(self.driver)
        navigation_page.open_gear_bags()
        products_page.click_checkbox()
        products_page.click_sort_by_price()
        products_page.select_product(1)
        products_page.click_add_to_compare()
        message = products_page.get_compare_success_message()
        assert message == "You added product Compete Track Tote to the comparison list."






