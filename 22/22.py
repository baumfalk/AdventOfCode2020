import copy
import time
from collections import defaultdict, Counter, deque
from copy import deepcopy
import numpy as np
from itertools import permutations

# complex*i to rotate left/ccw, complex*-i to rotate right/cw
x = 0+0j
direction = 1+0j
# if command == 'L':
#     direction *= 1j**(move // 90)
# if command == 'R':
#     direction /= 1j**(move // 90)


#content = list(map(lambda s: s.strip('\r\n'), open("input.txt").readlines()))
content = open("input.txt").read()
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result
    return timed

@timeit
def part1(input):
    player_1_data, player_2_data = input.split("\n\n")
    player_1_cards_raw = player_1_data.split("\n")[1:]
    player_2_cards_raw = player_2_data.split("\n")[1:]
    player_1_cards = deque(map(int,player_1_cards_raw))
    player_2_cards = deque(map(int, player_2_cards_raw))

    playing = True
    while playing:
        player_1_empty = len(player_1_cards) == 0
        player_2_empty = len(player_2_cards) == 0
        if player_1_empty or player_2_empty:
            playing = False
            continue

        player_1_card = player_1_cards.popleft()
        player_2_card = player_2_cards.popleft()

        if player_1_card > player_2_card:
            player_1_cards.append(player_1_card)
            player_1_cards.append(player_2_card)
        else:
            player_2_cards.append(player_2_card)
            player_2_cards.append(player_1_card)
    
    answer = 0
    if len(player_1_cards):
        answer = sum([(len(player_1_cards)-index)*num for index, num in enumerate(player_1_cards)])
    else:
        answer = sum([(len(player_2_cards) - index) * num for index, num in enumerate(player_2_cards)])

    return answer


def combat_recursive(player_1_cards, player_2_cards, depth=0, curgame=1):
    states = set()
    player_1_won_game = None
    player_1_won_round = None
    #print(f"=== Game {curgame}, depth {depth}")
    round=0
    next_game = curgame+1       
    
    while True:
        round += 1
        #print(f"-- Round {round} (Game {curgame}, depth {depth}) --")
        """
        Before either player deals a card, if there was a previous round in this game that had exactly the same cards 
        in the same order in the same players' decks, the game instantly ends in a win for player 1."""
        #state = tuple([tuple(player_1_cards), tuple(player_2_cards)])
        state = tuple(player_1_cards)
        if state in states:
            #print("This state already occurred before, P1 wins!")
            player_1_won_game = True
            break
        states.add(state)
        """
        Otherwise, this round's cards must be in a new configuration; the players begin the round by each drawing the 
        top card of their deck as normal.
        """
  
        #print(f"""Player 1's deck: {", ".join(map(str,player_1_cards))}
#Player 2's deck: {", ".join(map(str,player_2_cards))}""")
        player_1_card = player_1_cards.popleft()
        player_2_card = player_2_cards.popleft()
        #print(f"""Player 1 plays: {player_1_card}
#Player 2 plays: {player_2_card}""")
        """
        If both players have at least as many cards remaining in their deck as the value of the card they just drew, 
        the winner of the round is determined by playing a new game of Recursive Combat (see below).
        """
        cond_1_true = len(player_1_cards) >= player_1_card
        cond_2_true = len(player_2_cards) >= player_2_card
        recurse_cond_true = cond_1_true and cond_2_true
        if recurse_cond_true:
            player_1_cards_subgame = deque(list(player_1_cards)[:player_1_card])
            player_2_cards_subgame = deque(list(player_2_cards)[:player_2_card])
            #print(f"Playing a sub-game at depth {depth+1} to determine the winner...")
            if max(player_1_cards_subgame) > max(player_2_cards_subgame):
                player_1_won_subgame = True
                new_nextgame = -1000
            else:
                player_1_won_subgame,_,_, new_nextgame= combat_recursive(player_1_cards_subgame,player_2_cards_subgame, depth+1, next_game)
            #print(f"Anyway, back to game {curgame} at depth {depth+1}")
            next_game = new_nextgame
            player_1_won_round = player_1_won_subgame
        else:
            """Otherwise, at least one player must not have enough cards left in their deck to recurse; the winner of the 
                round is the player with the higher-value card."""
            player_1_won_round = player_1_card > player_2_card
        #print(f"Player {2-player_1_won_round} wins round {round-1} of game {curgame}!")  
        if player_1_won_round:
            player_1_cards.append(player_1_card)
            player_1_cards.append(player_2_card)
        else:
            player_2_cards.append(player_2_card)
            player_2_cards.append(player_1_card)
        player_1_empty = len(player_1_cards) == 0
        player_2_empty = len(player_2_cards) == 0
        if player_1_empty or player_2_empty:
            player_1_won_game = not player_1_empty
            break
    #print(f"The winner of game {curgame} is player {2-player_1_won_game}")
    return player_1_won_game, player_1_cards, player_2_cards, next_game
@timeit
def part2(input):
    player_1_data, player_2_data = input.split("\n\n")
    player_1_cards_raw = player_1_data.split("\n")[1:]
    player_2_cards_raw = player_2_data.split("\n")[1:]
    player_1_cards = deque(map(int, player_1_cards_raw))
    player_2_cards = deque(map(int, player_2_cards_raw))
    p1_won, player_1_cards, player_2_cards, next_game = combat_recursive(player_1_cards, player_2_cards, depth=0)
    answer = 0
    print(p1_won, player_1_cards, player_2_cards, next_game)
    if len(player_1_cards):
        answer = sum([(len(player_1_cards) - index) * num for index, num in enumerate(player_1_cards)])
    else:
        answer = sum([(len(player_2_cards) - index) * num for index, num in enumerate(player_2_cards)])

    return answer
print(part1(content))
print(part2(content))