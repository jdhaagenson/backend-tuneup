#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "Jordan Haagenson"

import cProfile
import pstats
import functools
import timeit

from functools import wraps


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    # Be sure to review the lesson material on decorators.
    # You need to understand how they are constructed and used.
    # raise NotImplementedError("Complete this decorator function")
    @wraps(func)
    def decorator(*args, **kwargs):
        """a function to be used as a decorator to measure the performance"""
        prof = cProfile.Profile()
        prof.enable()
        result = func(*args, **kwargs)
        prof.disable()
        ps = pstats.Stats(prof).strip_dirs().sort_stats('cumulative')
        ps.print_stats(8)
        return result
    return decorator


def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


# def is_duplicate(title, movies):
#     """Returns True if title is within movies list."""
#     for movie in movies:
#         if movie.lower() == title:
#             return True
#     return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    return [movie for movie in set(movies) if movies.count(movie) > 1]


def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    t = timeit.Timer(functools.partial(find_duplicate_movies, 'movies.txt'))
    time_result = min(t.repeat(repeat=7, number=3)) / 3
    print("Best time across 7 repeats of 3 runs per repeat ", time_result)


def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))
    timeit_helper()


if __name__ == '__main__':
    main()
