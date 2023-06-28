from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Tuple, Dict
import unittest


@dataclass(unsafe_hash=True)
class Order:
    id: int


@dataclass()
class DiscountCode:
    title: str
    max_orders: int
    expires: datetime
    dollars_off: int
    active: bool = True
    orders: list[Order] = field(default_factory=list)


def load_discounts() -> list[DiscountCode]:
    """
    Function to simulate loading discount codes (please do not modify this function)
    :return: list of DiscountCode objects
    """
    return [
        DiscountCode(title="FRIEND-12345", max_orders=1, dollars_off=10,
                     expires=datetime.now() + timedelta(days=30), orders=[Order(id=1)]),
        DiscountCode(title="SALE", max_orders=3, dollars_off=20,
                     expires=datetime.now() + timedelta(days=30), orders=[Order(id=2)]),
        DiscountCode(title="50-OFF", max_orders=10, dollars_off=12,
                     expires=datetime.now() - timedelta(days=30),
                     orders=[Order(id=3), Order(id=4)]),
        DiscountCode(title="HOLIDAY", max_orders=10, dollars_off=5, active=False,
                     expires=datetime.now() + timedelta(days=30),
                     orders=[Order(id=5), Order(id=6), Order(id=7), Order(id=1)]),
        DiscountCode(title="BUY-AGAIN", max_orders=3, dollars_off=15,
                     expires=datetime.now() + timedelta(days=30),
                     orders=[Order(id=2), Order(id=1), Order(id=11)]),
    ]


def is_discount_code_valid(code: str) -> bool:
    """
    TASK 1 - Function to validate a discount code
    :param code:
    :return bool: True if the discount code is valid, False otherwise
    """
    discount_codes: list[DiscountCode] = load_discounts()
    # TODO
    ...


def calculate_average_discount_dollar_off() -> float:
    """
    TASK 2 - Function to calculate the average discount per order, in dollars.
    :return float: representing the average discount per order
    """

    discount_codes: list[DiscountCode] = load_discounts()
    # TODO
    ...


def calculate_average_count_discounts() -> float:
    """
    TASK 3 - Function to calculate the average count of discount codes applied per order
    :return float: representing the average count of discount codes per order
    """
    discount_codes: list[DiscountCode] = load_discounts()
    # TODO
    ...


def find_order_that_use_most_discount_codes() -> Tuple[Order, int]:
    """
    TASK 4 - Function to find the order that has the most discount codes applied
    :return Tuple[Order, int]: Tuple containing the Order object and the number of discount codes used
    """
    discount_codes: list[DiscountCode] = load_discounts()
    # TODO
    ...


def order_discounts_by_usage() -> list[DiscountCode]:
    """
    TASK 5 - Function to order the discount codes by usage
    :return list[DiscountCode]: List of DiscountCode objects ordered by usage
    """
    discount_codes: list[DiscountCode] = load_discounts()
    # TODO
    ...
