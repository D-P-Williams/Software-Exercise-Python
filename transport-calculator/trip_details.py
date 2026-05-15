from dataclasses import dataclass


@dataclass
class TripDetails:
    """Class for keeping track of an individual delivery."""

    method: str
    duration: float
    cost: float
    distance: float
