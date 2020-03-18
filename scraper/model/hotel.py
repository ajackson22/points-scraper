class Hotel():
    name = None
    brand = None
    location = None
    cost_in_usd = None
    cost_in_points = None
    point_valuation = None

    def __init__(self, name, brand, location, cost_in_usd, cost_in_points, point_valuation):
        self.name = name
        self.brand = brand
        self.location = location
        self.cost_in_usd = cost_in_usd
        self.cost_in_points = cost_in_points
        self.point_valuation = point_valuation

    def __str__(self):
        return "Hotel: {Name:%s, Brand:%s, Location:%s, Cost In USD:%s, Cost In Points:%s, Valuation:%s" % (
        self.name, self.brand, self.location, self.cost_in_usd, self.cost_in_points,
        self.point_valuation)
