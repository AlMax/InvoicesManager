class Order:
    def __init__(self, description, quantity, price):
        self.Description = description;
        self.Quantity = "{:,.1f}".format(quantity);
        self.Price = "{:,.2f}".format(price);
        self.Total = "{:,.2f}".format(quantity * price);
    
    def ToDict(self):
        return vars(self);
