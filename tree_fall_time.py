from __future__ import annotations

import argparse
from datetime import datetime, timedelta

# Approximate speed of sound at 20°C, sea level.
SPEED_OF_SOUND_M_PER_S = 343.0


def estimate_tree_fall_time(heard_time: datetime, distance_meters: float) -> datetime:
    if distance_meters < 0:
        raise ValueError("distance_meters must be non-negative")

    delay_seconds = distance_meters / SPEED_OF_SOUND_M_PER_S
    return heard_time - timedelta(seconds=delay_seconds)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Estimate when a tree fell based on heard time and distance."
    )
    parser.add_argument(
        "--heard-time",
        required=True,
        help="Timestamp when you heard the tree (ISO 8601, e.g. 2026-06-08T10:00:00)",
    )
    parser.add_argument(
        "--distance-meters",
        type=float,
        required=True,
        help="Estimated distance from you to the tree in meters.",
    )
    args = parser.parse_args()

    try:
        heard_time = datetime.fromisoformat(args.heard_time)
    except ValueError:
        parser.error(
            "--heard-time must be a valid ISO 8601 timestamp "
            "(example: 2026-06-08T10:00:00)"
        )

    fall_time = estimate_tree_fall_time(heard_time, args.distance_meters)
    print(f"Estimated tree fall time: {fall_time.replace(microsecond=0).isoformat()}")


if __name__ == "__main__":
    main()
