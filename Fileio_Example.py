"""
    Name:Drishak Mohan
	Date: December 1th, 2018
	Description: Example to FileI/O .
"""


# This file works with a text file containing data about
# band preferences. For example:
# Band,Rating,Plays
# The Black Keys,8,193

from typing import TextIO, List


def get_bandnames(band_file: TextIO) -> List[str]:
    '''Return a list of all of the bandnames in a band file.
    Assumption: Header lines have been removed
    '''

    bands = []
    for line in band_file:
        fields = line.strip().split(",")
        bands.append(fields[0])

    return bands


def average_rating(band_file: TextIO) -> float:
    '''Return the average rating for all bands in band_file.
    Assumption: Header lines have been removed.
    '''

    sum = 0
    count = 0
    for line in band_file:
        fields = line.strip().split(",")
        sum += int(fields[1])
        count += 1
    return sum / count

    # The following also works fine. It uses a list instead
    # of a pair of accumulators.
    # ratings = []
    # for line in band_file:
    #     fields = line.strip().split(",")
    #     ratings.append(int(fields[1]))
    # return sum(ratings) / len(ratings)