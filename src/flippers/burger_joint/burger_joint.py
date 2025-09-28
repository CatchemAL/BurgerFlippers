from pydantic import Field
from flippers.chef import Chef
from flippers.core import FlipperBaseModel
from flippers.courier import Courier
from flippers.order_service import OrderService


class BurgerJoint(FlipperBaseModel):
    order_service: OrderService
    chef: Chef
    courier: Courier = Field(..., discriminator="kind")

    def run(self) -> None:
        orders = self.order_service.get_online_orders()

        for order in orders:
            burger = self.chef.prepare(order)
            self.courier.deliver(burger)
