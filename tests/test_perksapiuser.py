from perksapiuser import user_get
def test_auser_get():
    assert 200 == user_get()