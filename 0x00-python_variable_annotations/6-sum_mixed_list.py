#!/usr/bin/env python3
""" This module returns the sum of a list(integers) as float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of ints ad floats.

    Args:
        mxd_lst (List[int, float]): The list to sum.

    Returns:
        float: The sum of the input list.
    """
    return sum(mxd_lst)
