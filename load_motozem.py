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


def test_poradime_vam_menu_is_visible(page, load_motozem):
    poradime_button = page.get_by_label("Máte dotaz?")
    expect(poradime_button).to_be_visible()


def test_poradime_vam_menu_content(page, load_motozem):
    poradime_button = page.get_by_label("Máte dotaz?")
    poradime_button.click()

    poradime_menu = [
        {"selector": page.get_by_label("Napsat dotaz"), "text": "Napsat dotaz"},
        {"selector": page.get_by_role("complementary").get_by_role("link", name="+420 555 333 957"),
         "text": "+420 555 333 957"},
    ]

    for item in poradime_menu:
        menu_item = item["selector"]
        expect(menu_item).to_be_visible()
        expect(menu_item).to_have_text(item["text"])


def test_state_flag_is_visible(page, load_motozem):
    state_flag = page.get_by_role("link", name="Motozem.cz", exact=True)
    expect(state_flag).to_be_visible()


def test_state_flags_are_visible_when_hover_over(page, load_motozem):
    state_flag = page.get_by_role("link", name="Motozem.cz", exact=True)
    state_flag.hover()

    flag_items = [
        {"selector": page.get_by_role("link", name="Motozem.sk"), "aria_label": "Motozem.sk"},
        {"selector": page.get_by_role("link", name="Motozem.hu"), "aria_label": "Motozem.hu"},
        {"selector": page.get_by_role("link", name="Motozem.pl"), "aria_label": "Motozem.pl"},
        {"selector": page.get_by_role("link", name="Motozem.at"), "aria_label": "Motozem.at"},
        {"selector": page.get_by_role("link", name="Motozem.de"), "aria_label": "Motozem.de"},
        {"selector": page.get_by_role("link", name="Motozem.ro"), "aria_label": "Motozem.ro"},
        {"selector": page.get_by_role("link", name="Motozem.hr"), "aria_label": "Motozem.hr"},
        {"selector": page.get_by_role("link", name="Motozem.si"), "aria_label": "Motozem.si"},
    ]

    for flag in flag_items:
        menu_item = flag["selector"]
        expect(menu_item).to_be_visible()
        expect(menu_item).to_have_attribute("aria-label", flag["aria_label"])


def test_muj_ucet_is_visible(page, load_motozem):
    muj_ucet = page.get_by_role("link", name="Můj účet")
    expect(muj_ucet).to_be_visible()


def test_muj_ucet_menu_is_visible_when_hoover_over_muj_ucet(page, load_motozem):
    muj_ucet = page.get_by_role("link", name="Můj účet")
    muj_ucet_menu = page.get_by_text("Přihlásit Registrovat")
    muj_ucet.hover()
    expect(muj_ucet_menu).to_be_visible()


def test_prihlasit_registrovat_is_visible_when_hoover_over_muj_ucet(page, load_motozem):
    muj_ucet = page.get_by_role("link", name="Můj účet")
    muj_ucet.hover()

    muj_ucet_content = [
        {"selector": page.get_by_label("Přihlásit"), "text": "Přihlásit"},
        {"selector": page.get_by_label("Registrovat", exact=True), "text": "Registrovat"},
]

    for item in muj_ucet_content:
        menu_item = item["selector"]
        expect(menu_item).to_be_visible()
        expect(menu_item).to_have_text(item["text"])






    # page.get_by_label("Přihlásit")
    # page.get_by_label("Registrovat", exact=True)
