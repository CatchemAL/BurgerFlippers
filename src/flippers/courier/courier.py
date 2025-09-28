from typing import Literal


from pydantic import NonNegativeInt, PositiveFloat

from flippers.core.base_model import FlipperBaseModel
from flippers.models import Burger


class PremiumCourier(FlipperBaseModel):
    kind: Literal["premium"] = "premium"
    fee: PositiveFloat

    def deliver(self, burger: Burger) -> None:
        print(f"Delivering burger for ${self.fee}: {burger.description}")


class SlowCourier(FlipperBaseModel):
    kind: Literal["slow"] = "slow"
    queue_size: NonNegativeInt

    def deliver(self, burger: Burger) -> None:
        print(f"You are in position {self.queue_size} ({burger.description})")


type Courier = PremiumCourier | SlowCourier
