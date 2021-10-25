import requests
from hamcrest import *


def test_api_get():
    res = requests.get('https://reqres.in/api/users?page=2')
    assert res.status_code == 200
    data_res = res.json()['data']
    for i in data_res:
        assert_that(i, has_entries({"id": not_none(),
                                     "email": not_none(),
                                     "first_name": not_none(),
                                     "last_name": not_none(),
                                     "avatar": not_none()
                                    }))


def test_api_post():
    res = requests.post(' https://reqres.in/api/users', {
    "name": "morpheus",
    "job": "leader"
} )
    assert res.status_code == 201
    data_res = res.json()
    assert_that(data_res, has_entries({
    "name": not_none(),
    "job": not_none()
}))




