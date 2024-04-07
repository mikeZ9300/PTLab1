from typing import Dict, Tuple, List
from Types import DataType
from GetRatingLastQuartile import GetRatingLastQuartile
import pytest

from io import StringIO
import sys


RatingsType = Dict[str, float]
TestCases = List[Tuple[RatingsType, float, str]]


class TestCalcRating():
    @pytest.fixture()
    def test_cases(self) -> TestCases:
        test_cases: TestCases = [
            ({"a": 1, "b": 2, "c": 3, "d": 4}, 3, 'd'),
            ({"a": 1, "b": 2}, 1.75, 'b')
            ]
        return test_cases

    def test_calc_last_quartile(self, test_cases: TestCases) -> None:
        for test_case in test_cases:
            rating: RatingsType
            expected_quartile: float
            rating, expected_quartile = test_case[0], test_case[1]
            quartil: float = GetRatingLastQuartile().calc_last_quartile(rating)
            assert pytest.approx(quartil, abs=0.001) == expected_quartile

    def test_print_last_quartile_students(self, test_cases: TestCases) -> None:
        for test_case in test_cases:
            rating: RatingsType
            expected_students: str
            rating, expected_students = test_case[0], test_case[2]
            old_stdout = sys.stdout
            mystdout = StringIO()
            sys.stdout = mystdout
            GetRatingLastQuartile().print_last_quartile_students(rating)
            sys.stdout = old_stdout
            output = mystdout.getvalue()
            assert output == expected_students + "\n"
