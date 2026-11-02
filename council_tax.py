"""Council tax single person discount checker (prototype)."""

DISCOUNT_RATE = 0.25


def validate_adults(adults):
    """Check the number of adults entered is a whole number of 1 or more."""
    try:
        adults = int(str(adults).strip())
    except ValueError:
        raise ValueError("Number of adults must be a whole number") from None

    if adults < 1:
        raise ValueError("Number of adults must be at least 1")

    return adults


def check_discount(annual_charge, adults):
    """Return whether a household gets the single person discount
    and how much council tax it needs to pay."""
    adults = validate_adults(adults)
    eligible = adults == 1

    if eligible:
        amount_to_pay = annual_charge * (1 - DISCOUNT_RATE)
    else:
        amount_to_pay = annual_charge

    return {"eligible": eligible, "amount_to_pay": round(amount_to_pay, 2)}