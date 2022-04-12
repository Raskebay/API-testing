

from src.schemas.post import POST_SCHEMA

from src.baseclasses.response import Response


def test_getting_post(get_posts):
    Response(get_posts).assert_status_code(200).validate(POST_SCHEMA)


def test_another():
    assert 1 == 1