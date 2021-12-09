from perksapirefreshtoken import rfr_token
def test_rfr_token():
    assert 200 == rfr_token()