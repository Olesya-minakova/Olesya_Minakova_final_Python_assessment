import requests, pytest
from PO.authentication import authentication
from PO.details import details
from PO.endpoint import links
from PO.tourists_list import touristic

# Make instances of modules
auth = authentication()
detail = details()
url = links()
tour = touristic()

# Global variables
BEARER = f"bearer {auth.bearer_id(auth.user_creds)[0]}"
USER_ID = auth.bearer_id(auth.user_creds)[1]


def test_user_registration():
    """TEST

    Registration of a new user with defined information"""
    r = requests.post(url.reg, json=details.user_reg)
    assert r.status_code == 200


def test_user_login():
    """TEST

    Successful login"""
    r = requests.post(url.login, json=details.user_login)
    assert r.status_code == 200
    assert r.json()["data"]["Name"] == "tests-user"


def test_user_incorrect_name():
    """TEST

    Unsuccessful login due to invalid user name"""
    r = auth.login(user_data=detail.user_fakename)
    assert r.json()["message"] == "invalid username or password"


def test_user_incorrect_password():
    """TEST

    Unsuccessful login due to invalid password"""
    r = auth.login(user_data=detail.user_fakepass)
    assert r.json()["message"] == "invalid username or password"


def test_user_empty_name():
    """TEST

    Unsuccessful login due to empty user name"""
    r = auth.login(user_data=detail.user_noname)
    assert r.json()["Message"] == "The request is invalid."
    assert r.json()["ModelState"]["log.email"][0] == "field is required"


def test_user_empty_password():
    """TEST

    Unsuccessful login due to empty user password"""
    r = auth.login(user_data=detail.user_nopass)
    assert r.json()["Message"] == "The request is invalid."
    assert r.json()["ModelState"]["log.password"][0] == "field is required"


def test_list_of_tourists():
    """TEST

    See a list of tourists"""
    r = requests.get(url.tour)
    assert r.status_code == 200


@pytest.mark.xfail(reason="Doesn't work")
def test_tourist_creation():
    """TEST

    Create a new tourist"""
    r = tour.tourist_creation(tour.tourist_data)
    assert r.status_code == 201


def test_get_by_id():
    """TEST

    Check that the tourist is created"""
    r = requests.get(url.tour + "242302")
    assert r.status_code == 200


def test_get_by_id_negative():
    """TEST

    Check that the tourist with id=11 is not existed"""
    r = requests.get(url.tour + "11")
    assert r.status_code == 404


@pytest.mark.xfail(reason="Doesn't work")
def test_delete_tourist():
    """TEST

    Check that the tourist is deleted"""
    r = requests.delete(url.tour + "242302")
    assert r.status_code == 200


@pytest.mark.xfail(reason="Doesn't work")
def test_delete_user():
    """TEST

    Check that the user is deleted"""
    headers = {"Authorization": BEARER}
    r = requests.get(f"{url.user}{USER_ID}", headers=headers)
    assert r.status_code == 200
