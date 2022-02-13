from src.sorting import sort_by
import pytest

list_mock = [
  {'max_salary': 6000, 'min_salary': 4000, 'date_posted': '2021-10-09'},
  {'max_salary': 8000, 'min_salary': 5000, 'date_posted': '2022-01-20'},
  {'max_salary': 4000, 'min_salary': 3000, 'date_posted': '2021-12-16'},
  {'max_salary': 5000, 'min_salary': 2000, 'date_posted': '2021-11-25'},
]

list_expect_max_salary = [
  {'max_salary': 8000, 'min_salary': 5000, 'date_posted': '2022-01-20'},
  {'max_salary': 6000, 'min_salary': 4000, 'date_posted': '2021-10-09'},
  {'max_salary': 5000, 'min_salary': 2000, 'date_posted': '2021-11-25'},
  {'max_salary': 4000, 'min_salary': 3000, 'date_posted': '2021-12-16'},
]

list_expect_min_salary = [
  {'max_salary': 5000, 'min_salary': 2000, 'date_posted': '2021-11-25'},
  {'max_salary': 4000, 'min_salary': 3000, 'date_posted': '2021-12-16'},
  {'max_salary': 6000, 'min_salary': 4000, 'date_posted': '2021-10-09'},
  {'max_salary': 8000, 'min_salary': 5000, 'date_posted': '2022-01-20'},
]

list_expect_date_posted = [
  {'max_salary': 8000, 'min_salary': 5000, 'date_posted': '2022-01-20'},
  {'max_salary': 4000, 'min_salary': 3000, 'date_posted': '2021-12-16'},
  {'max_salary': 5000, 'min_salary': 2000, 'date_posted': '2021-11-25'},
  {'max_salary': 6000, 'min_salary': 4000, 'date_posted': '2021-10-09'},
]


def test_sort_by_criteria():
    sort_by(list_mock, 'min_salary')
    assert list_mock == list_expect_min_salary

    sort_by(list_mock, 'max_salary')
    assert list_mock == list_expect_max_salary

    sort_by(list_mock, 'date_posted')
    assert list_mock == list_expect_date_posted

with pytest.raises(ValueError):
    sort_by(list_mock, 'invalid_criteria')