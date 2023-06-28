# Head of Engineering Coding Test
### Please find instructions below for the two sections of this test:
1) Python/Backend Test
2) React/Frontend Test

Please complete both sections of the test, and please don't hesitate to reach out with any questions!


## Python/Backend Test
Below are the instructions for the backend section of this test. We recommend spending no more than 1-2 hours for this exercise. Please submit your completed file as a PR on this repo, and please email james@spotandtango.com when you're ready for the PR to be reviewed.

The backend test is comprised of 5 tasks relating to the application of discount codes to orders.

#### Task 1 - Coupon validation
Write a function that, given a discount code, will return True if the code is valid and False if it is invalid. The discount code is valid if:
- The discount code is not expired
- The discount code is not used more than the number of times it is allowed to be used
- The discount code is not used by the same user more than the number of times it is allowed to be used by the same user
- The discount code is active
- The discount code exists

```python
    is_discount_code_valid()
```
 

#### Task 2 - Average discount (in dollars) applied to orders
For this task, please return the average discount (in dollars) for the 8 existing orders.
```python
    calculate_average_discount_dollar_off()
```


#### Task 3 - Average number of discounts applied to orders
For this task, please return the average number of distinct discounts that are applied to the 8 existing orders.
```python
    calculate_average_count_discounts()
```


#### Task 4 - Order with the most discount codes
For this task, please return a Tuple with the ID value of the order that has the most discount codes applied and the number of discount codes applied.
```python
    find_order_that_use_most_discount_codes()
```

#### Task 5 - Discount codes by usage
For this task, please return a list of all the discount codes ordered by the number of orders on which they are used. Please order your list from most used to least used.
```python
    order_discounts_by_usage()
```

#### Execute the tests

```bash
    python -m unittest backend_test_applicant_version.py 
    ..........
    ----------------------------------------------------------------------
    Ran 10 tests in 0.002s
    
    OK
```

## React/Frontend test

Below are the instructions for the frontend section of this test. We recommend spending no more than 2-3 hours for this exercise. Please email your completed HTML/CSS/JS files to james@spotandtango.com.

Please use React to complete the challenge.


Test details:

We want to build a new page which allows customers to select products for their box and add them to a shopping cart.

This is a UX/UI heavy position, so your CSS is taken into consideration, but we understand you are only spending 2-3 hours on the test.

Endpoints have been set up that will return all available products or 1 product, by ID:

- Public endpoint to return a list of products: https://frontend-applicant-test-beb7ba453574.herokuapp.com/products

- Public endpoints that return 1 product filtered by id: https://frontend-applicant-test-beb7ba453574.herokuapp.com/products/f18f8f9e-134b-449d-9fde-a0d03cf5bac2

The URL returns JSON, so be sure to set your HTTP headers appropriately.

You will need to parse the JSON response, and create a page to allow the customer to pick options for their shopping cart.
 


Test requirements:

- Ability to select multiple items (and multiple quantities) to add to your cart

- If an individual item is sold out, it should not be selectable and the page should indicate the item is sold out.

- Price and MSRP should be shown. MSRP represents the original price of the item.

- A confirmation message upon successful submission of a pick

- Your picks should be reflected in your shopping cart

 

Good luck, and please reach out with any questions.
