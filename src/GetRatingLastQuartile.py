from typing import Dict, List, Callable

RatingT = Dict[str, float]


class GetRatingLastQuartile():
    def print_last_quartile_students(self, ratings: RatingT) -> None:
        quartile: float = self.calc_last_quartile(ratings)
        filtered_students: RatingT = self._filter_students(ratings, quartile)
        for k in filtered_students:
            print(k)

    def _filter_students(self, ratings: RatingT, quartile: float) -> RatingT:
        return {k: ratings[k] for k in ratings if ratings[k] > quartile}

    def calc_last_quartile(self, input_ratings: RatingT) -> float:
        ratings: List[float] = [input_ratings[x] for x in input_ratings]
        length: int = len(ratings)
        if length % 4 == 0:
            ratings.sort(reverse=True)  # descending
            return ratings[length//4]
        else:
            ratings.sort()  # ascending
            f_values: List[float] = [i/(length-1) for i in range(length)]
            lower: int = 0
            upper: int = length-1
            for i in range(length):
                if f_values[i] > 0.75:
                    upper = i
                    break
                else:
                    lower = i
            diff_f_values: float = f_values[upper] - f_values[lower]
            diff_75: float = 0.75 - f_values[lower]
            ratio: float = diff_75 / diff_f_values
            diff_values: float = ratings[upper] - ratings[lower]
            quartile: float = ratings[lower] + diff_values * ratio
            return quartile
