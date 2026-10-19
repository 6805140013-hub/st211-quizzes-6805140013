import pytest

@pytest.fixture(params=["Chrome", "Firefox", "Safari"])
def browser(request):
    browser_name = request.param
    print(f"\n [setup] launching {browser_name}")
    yield browser_name # provides the value to test, then
    print(f" [teardown] closing {browser_name}")

def test_page_load(browser):
    assert browser is not None

def test_button_clickable(browser):
    assert len(browser) > 0