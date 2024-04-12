import deck
import player
import game
from player import Player

my_deck = deck.Deck()
my_deck.shuffle()
pile = deck.Deck()
pile.empty()

computer_player = player.Player("computer")
player_1 = player.Player("player1")
# TODO fix this for more than 2 players
players_hands: list[Player] = [computer_player, player_1]
my_deck.initial_full_deck_deal_to_all_players(players_hands)

player_index = 0
current_player = game.get_current_player_from_index(player_index, players_hands)
current_player.flip_single_card(pile)

both_players_have_more_than_zero_cards = True
while both_players_have_more_than_zero_cards:
    current_card = pile.cards[-1]
    next_player = game.get_next_player_from_current_player(current_player, players_hands)
    current_player = next_player
    print(f"the current player is {current_player.name}")

    if not game.card_is_royal(current_card):
        current_player.flip_single_card(pile)
    else:
        if not current_player.can_complete_flipping_for_royals(current_card, pile):
            pile.shuffle()
            player_before = game.get_player_before_current_player(current_player, players_hands)
            print(f"{player_before.name} wins the pile")
            player_before.add_cards(list(pile.cards))
            pile.cards = []  # TODO why doesn't pile.empty() work here?
            # TODO Probably can just increment the index here? isntead of duplicating lines 18 and 19. Maybe move them inside the while loop?
            next_card = player_before.flip_single_card(pile)
            current_player = next_player

    # TODO Move these into a few methods
    # Truth Value Testing instead of len() > 0
    if not computer_player.cards:
        both_players_have_more_than_zero_cards = False
        print(f"computer_player loses")
        break
    if not player_1.cards:
        both_players_have_more_than_zero_cards = False
        print(f"player_1 wins")
        break
