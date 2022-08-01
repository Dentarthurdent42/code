from random import choices

test_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

def deck_prep(start_deck):
    '''take a list/set and return a dictionary of reverse indices'''
    working_deck = {}
    length = len(start_deck)
    for index in range(length):
        weight = (length - 1) - index
        working_deck[start_deck[index]] = weight
    return working_deck

def quasirandomizer(weighted_deck, num_draws):
    '''take dictionary of weights, pick an element, then print the element and the updated list
    in order of decreasing weight'''
    freq = {
        'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0,
        'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0
        }
    weights = list(weighted_deck.values())
    elements = list(weighted_deck.keys())
    for _ in range(num_draws):
        pick = choices(population=elements, weights=weights, k=1).pop()
        freq[pick] += 1
        elements.remove(pick)
        elements.append(pick)
        print(pick, elements)
    print(freq.values())

prepped_deck = deck_prep(test_list)

quasirandomizer(prepped_deck, 2600)
