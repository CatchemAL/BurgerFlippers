import hydra
from omegaconf import DictConfig
from hydra.utils import instantiate
from flippers.burger_joint import BurgerJoint


@hydra.main(config_path="conf", config_name="config", version_base="1.3")
def main(cfg: DictConfig) -> None:
    burger_joint: BurgerJoint = instantiate(cfg)
    burger_joint.run()
