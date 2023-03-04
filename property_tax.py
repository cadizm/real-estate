def ca_monthly_property_tax(purchase_price):
    """
    A good rule of thumb for California homebuyers who are trying to estimate what their property
    taxes will be is to multiply their home's purchase price by 1.25%. This incorporates the base
    rate of 1% and additional local taxes, which are usually about 0.25%.

    https://smartasset.com/taxes/california-property-tax-calculator
    """
    return purchase_price * 0.0125 / 12

if __name__ == '__main__':
    purchase_price = 1_000_000
    property_tax = ca_monthly_property_tax(purchase_price)
    print(f'Initial home purchase price   {purchase_price:>12,.2f}')
    print(f'Monthly property tax payment  {property_tax:>12,.2f}')

    """
Initial home purchase price   1,000,000.00
Monthly property tax payment      1,041.67
"""
