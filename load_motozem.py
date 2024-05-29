import pytest
from playwright.sync_api import Page, sync_playwright, expect
from conftest import load_motozem


def test_load_motozem(page):
    page.goto("https://www.motozem.cz/")
    accept_cookies = page.get_by_role("link", name="OK", exact=True)
    accept_cookies.click()


def test_banner_motozem_is_visible(page, load_motozem):
    banner_motozem = page.get_by_role("banner").get_by_role("link", name="MotoZem", exact=True)
    expect(banner_motozem).to_be_visible()


def test_informace_menu_is_visible_when_hover_over(page, load_motozem):
    informace_button = page.get_by_role("link", name="Informace")
    informace_menu = page.get_by_text("O nás Obchodní podmínky Ochrana osobních údajů Velkoobchod Prodejny Vnitřní")
    informace_button.hover()
    expect(informace_menu).to_be_visible()


def test_informace_menu_content(page, load_motozem):
    informace_button = page.get_by_role("link", name="Informace")
    informace_button.hover()

    informace_items = [
        {"selector": page.get_by_title("O nás"), "text": "O nás"},
        {"selector": page.get_by_title("Obchodní podmínky"), "text": "Obchodní podmínky"},
        {"selector": page.get_by_title("Ochrana osobních údajů"), "text": "Ochrana osobních údajů"},
        {"selector": page.get_by_title("Velkoobchod"), "text": "Velkoobchod"},
        {"selector": page.get_by_title("Prodejny"), "text": "Prodejny"},
        {"selector": page.get_by_title("Vnitřní oznamovací systém"), "text": "Vnitřní oznamovací systém"},
        {"selector": page.get_by_title("Výměna, vrácení, reklamace"), "text": "Výměna, vrácení, reklamace"},
        {"selector": page.get_by_role("link", name="Kariéra"), "text": "Kariéra"},
    ]

    for item in informace_items:
        menu_item = item["selector"]
        expect(menu_item).to_be_visible()
        expect(menu_item).to_have_text(item["text"])


def test_prodejny_menu_is_visible_when_hover_over(page, load_motozem):
    prodejny_button = page.get_by_role("banner").get_by_role("link", name="Prodejny")
    prodejny_menu = page.locator("li").filter(has_text="Prodejny Dobrá Brno Čestlice").get_by_role("list")
    prodejny_button.hover()
    expect(prodejny_menu).to_be_visible()


def test_prodejny_menu_content(page, load_motozem):
    prodejny_button = page.get_by_role("banner").get_by_role("link", name="Prodejny")
    prodejny_button.hover()

    prodejny_items = [
        {"selector": page.get_by_title("Dobrá"), "text": "Dobrá"},
        {"selector": page.get_by_title("Brno"), "text": "Brno"},
        {"selector": page.get_by_title("Čestlice"), "text": "Čestlice"},
        {"selector": page.get_by_title("Senec"), "text": "Senec"},
        {"selector": page.get_by_title("Plzeň"), "text": "Plzeň"},
        {"selector": page.get_by_title("Košice"), "text": "Košice"},
    ]

    for item in prodejny_items:
        menu_item = item["selector"]
        expect(menu_item).to_be_visible()
        expect(menu_item).to_have_text(item["text"])

