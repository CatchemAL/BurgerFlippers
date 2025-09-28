from typing import assert_never


from flippers.core.base_model import FlipperBaseModel
from flippers.models.burger import Burger
from flippers.models.orders import BurgerOrder, SmashBurgerOrder, VeggieBurgerOrder


class Chef(FlipperBaseModel):
    def prepare(self, order: BurgerOrder) -> Burger:
        print("Preparing...")
        match order:
            case SmashBurgerOrder(num_patties=np, cheese=cheese, include_onions=io):
                descr = f"🍔: {np} patties, {cheese} cheese" + (" +onions" if io else "")
                return Burger(descr)
            case VeggieBurgerOrder(veggie_patty=vp, cheese=cheese, include_onions=io):
                descr = f"🍔: {vp} patty, {cheese} cheese" + (" +onions" if io else "")
                return Burger(descr)
            case _:
                assert_never(order)
