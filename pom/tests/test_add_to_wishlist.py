import pytest
from pom.pages.products_page import ProductsPage
from pom.pages.navigation_page import NavigationPage


@pytest.mark.usefixtures("set_up")
@pytest.mark.usefixtures("log_in")
class TestAddToWishlist:

    def test_add_to_wishlist(self):
        navigation_page = NavigationPage(self.driver)
        products_page = ProductsPage(self.driver)
        navigation_page.open_gear_bags()
        products_page.select_product(3)
        products_page.click_add_to_wishlist()
        message = products_page.get_add_to_wishlist_success_message()
        assert message == "Endeavor Daytrip Backpack has been added to your Wish List. Click here to continue shopping."

    def test_choose_min_price_from_wishlist(self):
        navigation_page = NavigationPage(self.driver)
        products_page = ProductsPage(self.driver)
        navigation_page.open_gear_bags()
        products_page.click_sort_by_product_name()
        products_page.select_product(1)
        products_page.click_add_to_wishlist()
        message = products_page.get_add_to_wishlist_success_message()
        assert message == "Crown Summit Backpack has been added to your Wish List. Click here to continue shopping."
        products_page.go_to_wishlist()


