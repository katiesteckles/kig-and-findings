import itertools
import random

NUM_SYMBOLS = 63
DECK_SIZE = 55
SYMBOLS_ON_CARD = 8

num_match_freqs_1000 = []

for n in range(10000):
    deck = [random.sample(range(NUM_SYMBOLS), SYMBOLS_ON_CARD) for i in range(DECK_SIZE)]
    num_match_freqs = [0 for i in range(SYMBOLS_ON_CARD+1)]

    for pair in itertools.combinations(deck,2):
        num_matches = len([sym for sym in pair[0] if sym in pair[1]])
        num_match_freqs[num_matches]+=1
    num_match_freqs_1000.append(num_match_freqs)

for i in range(SYMBOLS_ON_CARD+1):
    print(sum([nmf[i] for nmf in num_match_freqs_1000]))
