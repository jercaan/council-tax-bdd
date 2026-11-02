"""Simple command-line interface for the council tax discount checker."""

from council_tax import check_discount

ANNUAL_CHARGE = 1800


def main():
    print("=== Council Tax Single Person Discount Checker ===")
    print(f"Annual council tax charge: £{ANNUAL_CHARGE:.2f}")
    adults = input("How many adults (18 or over) live at the property? ")

    try:
        result = check_discount(ANNUAL_CHARGE, adults)
    except ValueError as error:
        print(f"Error: {error}")
        return

    if result["eligible"]:
        print("You are eligible for the 25% single person discount.")
    else:
        print("You are not eligible for the single person discount.")
    print(f"Amount to pay: £{result['amount_to_pay']:.2f}")


if __name__ == "__main__":
    main()