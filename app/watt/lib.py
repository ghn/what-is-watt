def compute_energy(item1, item2, item1_quantity=1):
    """
    compute the amount of item2 for given quantity of item1
    """

    # TODO Fix it
    return item1_quantity + item1.id + item2.id


class ItemCompute(object):
    def __init__(self, base_item, target_item, base_item_quantity=1):
        self.base_item = base_item
        self.target_item = target_item
        self.value = compute_energy(base_item, target_item, base_item_quantity)
