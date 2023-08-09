"""
This program to used to find the minimum number of platforms
"""
from typing import List


def find_platform(arrival: List[int], departure: List[int]) -> int:
    arrival = sorted(arrival)
    departure = sorted(departure)
    platform_req = 1
    i = 1
    j = 0
    while i < len(arrival) and j < len(departure):
        if arrival[i] <= departure[j]:
            platform_req += 1
            i += 1
        else:
            j += 1
    return platform_req


if __name__ == '__main__':
    arrival_time = [900, 940, 950, 1100, 1500, 1800]
    departure_time = [910, 1200, 1120, 1130, 1900, 2000]
    print(find_platform(arrival_time, departure_time))
