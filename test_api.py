import requests
from hamcrest import *


def test_api_get():
    res = requests.get('https://reqres.in/api/users?page=2')
    assert res.status_code == 200
    user_set_1 = dict({
        "id": 7,
        "email": "michael.lawson@reqres.in",
        "first_name": "Michael",
        "last_name": "Lawson",
        "avatar": "https://reqres.in/img/faces/7-image.jpg"
    })
    assert_that(user_set_1, has_entries({ "id": not_none(),
            "email": not_none(),
            "first_name": not_none(),
            "last_name": not_none(),
            "avatar":not_none(),
    }))
    user_set_2 = dict({
        "id": 8,
        "email": "lindsay.ferguson@reqres.in",
        "first_name": "Lindsay",
        "last_name": "Ferguson",
        "avatar": "https://reqres.in/img/faces/8-image.jpg"
    })
    assert_that(user_set_2, has_entries({"id": not_none(),
                                         "email": not_none(),
                                         "first_name": not_none(),
                                         "last_name": not_none(),
                                         "avatar": not_none(),
                                         }))
    user_set_3 = dict({
        "id": 9,
        "email": "tobias.funke@reqres.in",
        "first_name": "Tobias",
        "last_name": "Funke",
        "avatar": "https://reqres.in/img/faces/9-image.jpg"
    })
    assert_that(user_set_3, has_entries({"id": not_none(),
                                         "email": not_none(),
                                         "first_name": not_none(),
                                         "last_name": not_none(),
                                         "avatar": not_none(),
                                         }))
    user_set_4 = dict({
        "id": 10,
        "email": "byron.fields@reqres.in",
        "first_name": "Byron",
        "last_name": "Fields",
        "avatar": "https://reqres.in/img/faces/10-image.jpg"
    })
    assert_that(user_set_4, has_entries({"id": not_none(),
                                         "email": not_none(),
                                         "first_name": not_none(),
                                         "last_name": not_none(),
                                         "avatar": not_none(),
                                         }))
    user_set_5 = dict({
        "id": 11,
        "email": "george.edwards@reqres.in",
        "first_name": "George",
        "last_name": "Edwards",
        "avatar": "https://reqres.in/img/faces/11-image.jpg"
    })
    assert_that(user_set_5, has_entries({"id": not_none(),
                                         "email": not_none(),
                                         "first_name": not_none(),
                                         "last_name": not_none(),
                                         "avatar": not_none(),
                                         }))
    user_set_6 = dict({
        "id": 12,
        "email": "rachel.howell@reqres.in",
        "first_name": "Rachel",
        "last_name": "Howell",
        "avatar": "https://reqres.in/img/faces/12-image.jpg"
    })
    assert_that(user_set_6, has_entries({"id": not_none(),
                                         "email": not_none(),
                                         "first_name": not_none(),
                                         "last_name": not_none(),
                                         "avatar": not_none(),
                                         }))



def test_api_post():
    res = requests.post(' https://reqres.in/api/users', {
    "name": "morpheus",
    "job": "leader"
} )
    assert res.status_code == 201
    new_user = dict({
    "name": "morpheus",
    "job": "leader"
})
    assert_that(new_user, has_entries({
    "name": not_none(),
    "job": not_none()
}))




