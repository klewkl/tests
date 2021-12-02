from typing import List, Tuple
import unittest


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in
                        bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


class TFT(unittest.TestCase):
    def test_cities(self):
        actual = ['Moscow', 'New York', 'Moscow', 'London']
        expected_city = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1,  0, 0]),
        ]
        self.assertEqual(expected_city, fit_transform(actual))

    def test_weather(self):
        weather = ['rainy', 'sunny', 'cloudy']
        expected_weather = [
            ('rainy', [0, 0, 1]),
            ('sunny', [0, 1, 0]),
            ('cloudy', [1, 0, 0]),
        ]

        self.assertTrue(fit_transform(weather) == expected_weather)

    def test_aaa_exams(self):
        subject = ['SQL', 'Python', 'Stat', 'Metrics']
        expected_subject = [
            ('SQL', [0, 0, 0, 1]),
            ('Python', [0, 0, 1, 0]),
            ('Stat', [0, 1, 0, 0]),
            ('Metrics', [1, 0, 0, 0])
        ]
        self.assertTrue(fit_transform(subject) == expected_subject)

    def test_exception(self):
        with self.assertRaises(TypeError):
            e = fit_transform(0)

if __name__ == '__main__':
    unittest.main()
