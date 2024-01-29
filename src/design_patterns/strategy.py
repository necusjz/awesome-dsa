class Values:
    def __init__(self, vals):
        self.vals = vals

    def filter(self, strategy):
        result = []
        for val in self.vals:
            if strategy(val):
                continue

            result.append(val)

        return result
