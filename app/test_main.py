from app.main import can_access_google_page
from unittest import mock


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_accesible(mock_internet, mock_valid):
    mock_valid.return_value = True
    mock_internet.return_value = True
    assert can_access_google_page('https://www.google.com') == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_accesible_url(mock_internet, mock_valid):
    mock_valid.return_value = False
    mock_internet.return_value = True
    assert can_access_google_page('https://www.gogle.com') == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_accesible_internet(mock_internet, mock_valid):
    mock_valid.return_value = True
    mock_internet.return_value = False
    assert can_access_google_page('https://www.google.com') == "Not accessible"
