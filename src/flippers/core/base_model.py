from pydantic import BaseModel, ConfigDict


class FlipperBaseModel(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
