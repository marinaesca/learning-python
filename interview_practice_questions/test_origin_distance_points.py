import pytest
from interview_practice_questions.origin_distance_points import find_k_closest_origin_distance

def test_find_k_closest_origin_distance_basic():
    coordinates = [[0,1],[-2,0],[2,1]]
    k = 2
    result = find_k_closest_origin_distance(coordinates, k)
    expected = [[0, 1], [-2, 0]]
    assert set(tuple(x) for x in result) == set(tuple(x) for x in expected)

def test_find_k_closest_origin_distance_complex():
    coordinates = [[1, 1], [-1, -1], [1, -1], [-1, 1], [3, 4], [0, 2]]
    k = 4
    result = find_k_closest_origin_distance(coordinates, k)
    expected = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
    assert set(tuple(x) for x in result) == set(tuple(x) for x in expected)

def test_find_k_closest_origin_distance_seven_points():
    coordinates = [[3,4], [1,2], [-1,0], [-1,-1], [2,2], [5,5], [0,1]]
    k = 3
    result = find_k_closest_origin_distance(coordinates, k)
    expected = [[0, 1], [-1, -1], [-1, 0]]
    assert set(tuple(x) for x in result) == set(tuple(x) for x in expected)