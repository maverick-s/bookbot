def num_words(book):
    num_of_words = len(book.split())
    return (f"Found {num_of_words} total words")

def char_count(book):
    characters = [c.lower() for c in book if not c.isspace()]
    character_count = {}

    for c in characters:
        if c in character_count:
            character_count[c] +=1
        else:
            character_count[c] = 1

    return character_count



def report(character_count):

    sorted_dict = dict(sorted(character_count.items(), key=lambda kv: kv[1], reverse=True))
    return sorted_dict
