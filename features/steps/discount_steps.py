from behave import given, when, then
from council_tax import check_discount


@given("the annual council tax charge is £{charge:d}")
def step_set_annual_charge(context, charge):
    context.charge = charge


@when('the resident enters "{adults}" as the number of adults')
def step_enter_number_of_adults(context, adults):
    context.result = None
    context.error = None
    try:
        context.result = check_discount(context.charge, adults)
    except ValueError as error:
        context.error = str(error)


@then("the resident should be eligible for the discount")
def step_check_eligible(context):
    assert context.error is None, f"Unexpected error: {context.error}"
    assert context.result["eligible"] is True


@then("the resident should not be eligible for the discount")
def step_check_not_eligible(context):
    assert context.error is None, f"Unexpected error: {context.error}"
    assert context.result["eligible"] is False


@then("the amount to pay should be £{amount:f}")
def step_check_amount_to_pay(context, amount):
    assert context.result["amount_to_pay"] == amount, (
        f"Expected £{amount:.2f} but got £{context.result['amount_to_pay']:.2f}"
    )


@then('an error message should say "{message}"')
def step_check_error_message(context, message):
    assert context.error == message, (
        f'Expected error "{message}" but got "{context.error}"'
    )