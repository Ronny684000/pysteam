import pytest

from pages.main_menu_page import MainMenuPage


@pytest.mark.parametrize("game_name, games_to_check", [("The Witcher", 10), ("Fallout", 20)])
def test_steam_scenario(game_name, games_to_check):
    MainMenuPage()\
        .verify_page_is_loaded()\
        .find_game(game_name)\
        .verify_page_is_loaded()\
        .verify_item_list_not_empty()\
        .sort_results()\
        .verify_sort_is_correct(games_to_check)
