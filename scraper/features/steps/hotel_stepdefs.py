from behave import given, when, then
from scraper.util.operator import operator

@given('my desired hotel brand is "{brand}"')
def step_impl(context, brand):
    """
    :type context: behave.runner.Context
    :type brand: str
    """
    operator.brand = brand
    operator.navigate_to()


@when('I search for all hotels in city "{location}"')
def step_impl(context, location):
    """
    :type context: behave.runner.Context
    """
    operator.search(location)


@then('I scrap all costs for hotels in area in "{currency}"')
def step_impl(context, currency):
    """
    :type context: behave.runner.Context
    """
    if currency == "points":
        operator.change_currency(currency)
    operator.scrap()

@then("I calculate valuation for hotel points")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    operator.calculate_valuation()


@then("I list the hotels")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    operator.show()


@then("I show the best award redemption")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    operator.best_award()