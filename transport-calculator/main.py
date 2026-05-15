"""
This is a simplified python application to calculate transport costs for
a shipping company from their location to a customer on a 100 by 100 grid.

Each point represents a potential delivery location (apart from the companies own depot)
and each point is additionally connected by road and canal.
"""

from transport_handler import TransportHandler
import json


def print_loop(config):
    """Console print loop to serve as user I/O"""

    # <-- Removed log in / admin account creation / customer management for simplicity -->

    while True:
        customer_raw = input("Enter Customer Coordinates (x,y): ")

        # We should probably add some input validation eventually - Lucy 15/03/2025.
        [customer_x, customer_y] = [x.strip() for x in customer_raw.split(",")]

        transport_method = input(
            "Select Transport Method (Lorry L, Canal C, Helicopter H): "
        )

        transport_handler = TransportHandler()
        trip = transport_handler.calculate_costs(
            config, transport_method, int(customer_x), int(customer_y)
        )

        transport_handler.print_trip(trip)


def main():
    """main entrypoint"""

    with open("configuration.json", encoding="utf-8") as json_data:
        config = json.load(json_data)
        json_data.close()

        print_loop(config)


if __name__ == "__main__":
    main()
