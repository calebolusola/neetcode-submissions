class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleet_times = []

        for p, s in cars:
            time = (target - p) / s

            # We process cars from closest to farthest from the target.
            #
            # The car/fleet ahead is the only thing that matters because
            # cars cannot pass it. If a car behind catches it, both become
            # part of the same fleet.
            #
            # If this car would arrive at the target at the same time or
            # earlier than the fleet ahead, it must catch that fleet.
            #
            # If it would arrive later, it cannot catch the fleet ahead,
            # so it creates a new fleet.

            if not fleet_times or time > fleet_times[-1]:
                fleet_times.append(time)

        return len(fleet_times)