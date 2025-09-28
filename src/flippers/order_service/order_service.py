import random
import time
from abc import ABC, abstractmethod
from collections.abc import Iterable
from datetime import timedelta
from typing import override
from pydantic import Field, NonNegativeInt
from flippers.core.base_model import FlipperBaseModel
from flippers.models.orders import BurgerOrder, SmashBurgerOrder, VeggieBurgerOrder


class OrderService(FlipperBaseModel, ABC):
    num_orders: NonNegativeInt

    @abstractmethod
    def get_online_orders(self) -> Iterable[BurgerOrder]: ...


class FullOrderService(OrderService):
    order_frequency: timedelta
    smash_probability: float = Field(default=0.5, ge=0.0, le=1.0)

    @override
    def get_online_orders(self) -> Iterable[BurgerOrder]:
        for _ in range(self.num_orders):
            print("\nCreating order...")
            is_smash = random.uniform(0, 1) <= self.smash_probability
            if is_smash:
                order = SmashBurgerOrder(
                    num_patties=random.randint(1, 3),
                    cheese=random.choice(["none", "american", "blue"]),
                    include_onions=random.choice([True, False]),
                )
            else:
                order = VeggieBurgerOrder(
                    veggie_patty="mushroom",
                    cheese="american",
                    include_onions=random.choice([True, False]),
                )

            yield order
            time.sleep(self.order_frequency.total_seconds())


class VeganOrderService(OrderService):
    order_frequency: timedelta

    @override
    def get_online_orders(self) -> Iterable[BurgerOrder]:
        for _ in range(self.num_orders):
            print("\nCreating order...")
            order = VeggieBurgerOrder(
                veggie_patty="black_bean",
                cheese="none",
                include_onions=random.choice([True, False]),
            )

            yield order
            time.sleep(self.order_frequency.total_seconds())
