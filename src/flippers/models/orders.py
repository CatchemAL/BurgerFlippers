from pydantic import PositiveInt
from pydantic.dataclasses import dataclass

from flippers.core.type_aliases import Cheese, VeggiePatty


@dataclass
class SmashBurgerOrder:
    num_patties: PositiveInt
    cheese: Cheese
    include_onions: bool


@dataclass
class VeggieBurgerOrder:
    veggie_patty: VeggiePatty
    cheese: Cheese
    include_onions: bool


type BurgerOrder = SmashBurgerOrder | VeggieBurgerOrder
