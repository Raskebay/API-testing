import pytest
from src.schemas.post import POST_SCHEMA

from src.baseclasses.response import Response


def test_getting_post(get_posts, make_number):
    Response(get_posts).assert_status_code(200).validate(POST_SCHEMA)
    print(make_number)


@pytest.mark.production
@pytest.mark.skip
def test_another():
    assert 1 == 1


@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result', [(1, 2, 3),
                                                               (-1, 2, 1),
                                                               (-1, -2, -3),
                                                               ('a', 2, None),
                                                               ('a', 'b', None)])
def test_calculator(first_value, second_value, result, calculate):
    assert calculate(first_value, second_value) == result
