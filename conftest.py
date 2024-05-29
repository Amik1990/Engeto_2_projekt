from typing import Dict
import pytest
from playwright.sync_api import BrowserType, sync_playwright, Page


@pytest.fixture()
def load_motozem(page: Page):    # načtění stránky motozem
    page.goto("https://www.motozem.cz/")
    accept_cookies = page.get_by_role("link", name="OK", exact=True)
    accept_cookies.click()

#Vytvořili jsme conftest.py s funkci viz níže, aby se ignorovaly případné chyby https během testování
#@pytest.fixture(scope="session")
#def browser_context_args(browser_context_args):
 #   return {
 #       **browser_context_args,
 #       "ignore_https_errors": True
  #  }


#Kód níže nám slouží ke změně rozlišení v prováděných testech
# @pytest.fixture(scope="session")
# # def browser_context_args(browser_context_args):
# #     return {
# #         **browser_context_args,
# #         "viewport": {
# #             "width": 800,
# #             "height": 455,
# #         }
# #     }


# Pokud chci, aby se mi test zobrazil v rozlišení podle konkrétního zařízení, tak napíšu, viz níže:
# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args, playwright):
#     iphone_11 = playwright.devices['iPhone 11 Pro']
#     return {
#         **browser_context_args,
#         **iphone_11,
#     }


# kód níže použiju, když chci změnit jazyk webové stránky
from playwright.sync_api import BrowserType
from typing import Dict


# @pytest.fixture(scope="session")
# def context(
#         browser_type: BrowserType,
#         browser_type_launch_args: Dict,
#         browser_context_args: Dict,
#         ):
#     context = browser_type.launch_persistent_context(
#         "./foobar",
#         **{
#             **browser_type_launch_args,
#             **browser_context_args,
#             "locale": "de-DE",
#             })
#     yield context
#     context.close()

