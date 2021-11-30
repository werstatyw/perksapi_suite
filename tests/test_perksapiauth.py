from perksapiauth import auth_req
def test_auth_req():
    assert 200 == auth_req()