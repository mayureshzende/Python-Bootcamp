
from shopping_cart import ShoppingCart
import pytest

# we can also run the specific file test in python we need to pass the file name to pytest <filename>
# we can test specific function in the pytest file as well 
# pytest test_shoppin_cart.py::<functionanme>

""" 
    if we have to make some generic line that does the same thing in every function we can  do that using the fixture in pytest 
"""
@pytest.fixture
def cart():
    return ShoppingCart(5)

# we just need to pass the function name into the test functions parameters
def test_add_item_to_cart(cart):
    # cart = ShoppingCart(5)
    cart.add_item_to_cart("apple")
    assert cart.size() == 1

def test_item_are_present_in_cart(cart):
    # cart = ShoppingCart(5)
    cart.add_item_to_cart("apple")
    cart.add_item_to_cart("mango")
    assert "apple" in cart.get_items()

def test_for_items_overFlow_check(cart):
    # cart = ShoppingCart(5)
    for _ in range(5):
        cart.add_item_to_cart("apple")
    
    # cart.add_item_to_cart("mango")
    #  we can pass the test if the exception is raise in the code and pass the test manually 
    with pytest.raises(OverflowError):
        cart.add_item_to_cart("mango")  
        # assert cart.size() == 5 

def test_price_for_total_items_in_cart(cart):
    prices = {
        "apple" : 1.0,
        "mangoes" : 2.0 
    }

    # cart = ShoppingCart(5)
    cart.add_item_to_cart("apple")
    cart.add_item_to_cart("mangoes")

    assert cart.get_total_price_of_items_in_dict(prices) == 3.0
