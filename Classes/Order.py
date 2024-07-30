def formatFloat(number):
    # Convert number to string and split into integer and decimal parts
    integer_part, decimal_part = f"{number:.2f}".split(".")
    # Add thousands separator
    integer_part_with_thousands = "{:,}".format(int(integer_part)).replace(",", ".")
    # Combine integer and decimal parts with comma as decimal separator
    formatted_number = f"{integer_part_with_thousands},{decimal_part}"
    return formatted_number

class Order:
    def __init__(self, description, quantity, price):
        self.Description = description;
        self.Quantity = formatFloat(quantity)
        self.Price = formatFloat(price)
        self.Total = formatFloat(quantity * price)

    def ToDict(self):
        return vars(self);

    @classmethod
    def FromDict(cls, data):
        return cls(
            data["Description"],
            float(data["Quantity"].replace(".", "").replace(",", ".")),
            float(data["Price"].replace(".", "").replace(",", ".")),
        )
