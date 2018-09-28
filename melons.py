from random import randint

"""Classes for melon orders."""


class AbstractMelonOrder():
    ""
    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.base_price = randint(5, 10)

    def get_total(self):
        """Calculate price, including tax."""
        base_price = self.get_base_price()

        if self.species == "Christmas melon":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def get_base_price(self):

        return randint(5, 10)

    def mark_shipped(self):
            """Record the fact than an order has been shipped."""

            self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def get_total(self):
        """Calculate price, including tax."""
        base_price = super().get_total()

        if self.qty < 10:
            base_price += 3

        return base_price


class GovernmentMelonOrder(AbstractMelonOrder):
    """ A melon order for the US Government."""
    order_type = "Government"
    tax = 0.0
    passed_inspection = False

    def mark_inspection(self, passed=True):

        self.passed_inspection = True
