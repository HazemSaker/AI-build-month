from collections import Counter

def wcount_dict(text: str) -> list:
    """ Returns the 10 most common words in the text using dictionary."""
    wcounter = {w, wcounter.get(w, 0) + 1 for w in text.lower().split()}
    #for w in text.lower().split():
    #    wcounter[w] = wcounter.get(w, 0) + 1

    return sorted(wcounter.items(), key = lambda item: item[1], reverse = True)[:10]


def wcount_collect(text: str) -> list:
    """ Returns the 10 most common words in the text using collections."""
    wcount = Counter(text.lower().split())
    return wcount.most_common(10);