"""Council tax single person discount checker (prototype)."""

DISCOUNT_RATE = 0.25


def check_discount(annual_charge, adults):
    """Return whether a household gets the single person discount
    and how much council tax it needs to pay."""
    adults = int(adults)
    eligible = adults == 1

    if eligible:
        amount_to_pay = annual_charge * (1 - DISCOUNT_RATE)
    else:
        amount_to_pay = annual_charge

    return {"eligible": eligible, "amount_to_pay": round(amount_to_pay, 2)}