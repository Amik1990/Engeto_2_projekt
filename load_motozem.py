import pytest
from playwright.sync_api import Page, sync_playwright, expect


@pytest.fixture()
def test_load_motozem(page):
    page.goto("https://www.motozem.cz/")
    accept_cookies = page.get_by_role("link", name="OK", exact=True)
    accept_cookies.click()


def test_banner_motozem_is_visible(page, test_load_motozem):
    banner_motozem = page.get_by_role("banner").get_by_role("link", name="MotoZem", exact=True)
    expect(banner_motozem).to_be_visible()


