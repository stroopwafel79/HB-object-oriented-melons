"""Classes for melon orders."""

class AbstractMelonOrder():
    ""
    def __init__(self, species, qty, order_type, country_code="USA"):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.country_code = country_code
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        if self.species == "Christmas melon":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total
    
    def mark_shipped(self):
            """Record the fact than an order has been shipped."""

   
            self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(species, qty, "domestic")
        self.tax = 0.08

    def get_total(self):

        return super().get_total()

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        super().mark_shipped()


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "international", country_code)
        self.tax = 0.17


    def get_total(self):
        """Calculate price, including tax."""
        base_price = super().get_total()

        if self.qty <10:
            base_price += 3

        return base_price

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        super().mark_shipped()


class GovernmentMelonOrder(AbstractMelonOrder):
    """ A melon order for the US Government."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "Government")
        self.tax = 0.00
        self.passed_inspection = False

    def get_total(self):

        return super().get_total() 

    def mark_inspection(self, passed=True):

        self.passed_inspection = True
