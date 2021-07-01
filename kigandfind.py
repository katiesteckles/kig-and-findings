# import card data
with open("cards.csv", "r") as file:
    cards = file.readlines()
cards = [card[:-1].split(",")[1:] for card in cards]

for card in cards:
    card.sort()

# match counting function
def find_matches(card1,card2):
    matcheroos = [symbol for symbol in card1 if symbol in card2]
    return matcheroos

# loop over all pairs of cards
matches = []
for i in range(55):
    for j in range(i):
        matches.append([i,j, find_matches(cards[i],cards[j])])

# largest overlap between two cards = 4
largest_overlap = max([len(match[2]) for match in matches])
# how many pairs achieve that = 6
len([match for match in matches if len(match[2])==largest_overlap])
# what cards is that
eldritch_horror = [match for match in matches if len(match[2])==largest_overlap]

# how many pairs have no match = 504
len([match for match in matches if len(match[2])==0])

# distribution of numbers of matches
distro = []
for i in range(9):
    distro.append(len([match for match in matches if len(match[2]) == i]))


# do any cards have a symbol that could be removed?