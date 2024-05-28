import pytest
from playwright.sync_api import Page, sync_playwright, expect


def test_load_motozem(page):
    page.goto("https://www.motozem.cz/")
    page.get_by_role("link", name="OK", exact=True).click()
    expect(page.get_by_role("banner").get_by_role("link", name="MotoZem", exact=True)).to_be_visible()


