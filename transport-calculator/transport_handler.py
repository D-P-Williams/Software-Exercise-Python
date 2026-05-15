"""
Handle the calculating of costs and durations for various transport methods.
"""

import sys
import math
from trip_details import TripDetails
from datetime import datetime, timedelta


class TransportHandler:
    """Class to handle the calculation of transport costs via various transport methods."""

    def calculate_costs(
        self, config, transport_method: str, customer_x: int, customer_y: int
    ) -> TripDetails:
        """
        Calculate the cost of a given journey, given the transport method and customer coordinates.
        """

        match transport_method.lower():
            case "L":
                return self._calculate_lorry(config, customer_x, customer_y)
            case "C":
                return self._calculate_canal_boat(config, customer_x, customer_y)
            case "H":
                return self._calculate_helicopter(config, customer_x, customer_y)
            case _:
                print("Unhandled vehicle type, please try again.\n\n", file=sys.stderr)
                raise SystemExit()

    def print_trip(self, trip: TripDetails):
        """Pretty print the details of a single trip"""

        pretty_duration = self._pretty_time(trip.duration)

        print(
            f"Journey by {trip.method} ({trip.distance:.1f} miles) costs £{trip.cost:.2f}"
            + f" and takes {pretty_duration} hours\n\n"
        )

    def _pretty_time(self, seconds) -> str:
        d = datetime(1, 1, 1) + timedelta(minutes=float(seconds))
        return f"{d.hour:02}:{d.minute:02}:{d.second:02}"

    def _calculate_lorry(self, config, customer_x: int, customer_y: int):
        diff_x, diff_y = self._grid_distance(config, customer_x, customer_y)

        total_dist = diff_x + diff_y

        # Calc Time
        speed = config["vehicles"]["lorry"]["speed"]
        total_time_s = total_dist / speed

        traffic_stops = math.floor(
            total_dist / config["vehicles"]["lorry"]["trafficDelayFrequency"]
        )
        total_time = total_time_s + (
            traffic_stops * ((config["vehicles"]["lorry"]["trafficDelayTime"]) / 60.0)
        )
        total_time_duration = total_time * 60

        # Calc Cost
        cost = (1.0 / 12.0) * ((total_dist**2) - (95 * total_dist) + 2880)

        return TripDetails(
            method="Lorry",
            duration=total_time_duration,
            cost=cost,
            distance=total_dist,
        )

    def _calculate_canal(self, config, customer_x: int, customer_y: int):
        """Function to calculate the time and cost of a canal journey - The intern 20/06/2025"""
        diff_x, diff_y = self._grid_distance(config, customer_x, customer_y)

        total_dist = diff_x + diff_y

        # Calc Time
        speed = config["vehicles"]["canal"]["speed"]
        total_time_s = total_dist / speed

        total_time_duration = total_time_s * 60

        # Calc Cost
        cost = ((5 * total_dist) / 12) + 1280

        return TripDetails(
            method="Canal boat",
            duration=total_time_duration,
            cost=cost,
            distance=total_dist,
        )

    def _calculate_helicopter(self, config, customer_x: int, customer_y: int):
        total_dist = self._euclidean_distance(config, customer_x, customer_y)

        # Calc Time
        speed = config["vehicles"]["helicopter"]["speed"]
        total_time_s = total_dist / speed

        total_time_duration = (
            total_time_s + (config["vehicles"]["helicopter"]["initialDelay"])
        ) * 60

        # Calc Cost
        cost = (0.5 * total_dist) + 195

        return TripDetails(
            method="Helicopter",
            duration=total_time_duration,
            cost=cost,
            distance=total_dist,
        )

    def _grid_distance(self, config, customer_x: int, customer_y: int):
        diff_x = abs(config["company"]["gridX"] - customer_x)
        diff_y = abs(config["company"]["gridY"] - customer_y)

        return diff_x, diff_y

    def _euclidean_distance(self, config, customer_x: int, customer_y: int):
        diff_x = abs(config["company"]["gridX"] - customer_x)
        diff_y = abs(config["company"]["gridY"] - customer_y)

        return math.sqrt(diff_x**2 + diff_y * 2)
