class Movement:
    def __init__(
        self,
        identifier: int,
        created_on,
        product_id: int,
        movement_type: str,
        quantity: int | float,  # noqa: PYI041
    ):
        self.id = identifier
        self.created_on = created_on
        self.product_id = product_id
        self.movement_type = movement_type
        self.quantity = quantity
