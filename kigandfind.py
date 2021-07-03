# import card data
with open('kig-and-findings/cards.csv', 'r') as file:
    cards = file.readlines()
cards = [card[:-1].split(',')[1:] for card in cards]

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

# Harder questions for another day:
# do any cards have a symbol that could be removed?
# if you just pick a random set of symbols to put on each card, how close to these stats do you get?,
# what's the largest monomatching game contained within this game?

# set up a graph
import networkx
monomatch_graph = networkx.Graph()

# populate the graph
monomatches = [match for match in matches if len(match[2]) == 1]
monomatch_nodes = [match[0] for match in matches] # add all the nodes at one end of an arc
monomatch_nodes.extend([match[1] for match in matches]) # the other ends
monomatch_nodes = set(monomatch_nodes) # that's all of them

for node in monomatch_nodes:
    monomatch_graph.add_node(node)

for arc in monomatches:
    monomatch_graph.add_edge(arc[0],arc[1])

# find all the complete subgraphs (cliques)
list_of_cliques = list(networkx.find_cliques(monomatch_graph))

# Largest clique
max_clique_size = max([len(clique) for clique in list_of_cliques)
[clique for clique in list_of_cliques if len(clique)==max_clique_size]
# [[14, 15, 38, 52, 32, 51, 6]]
