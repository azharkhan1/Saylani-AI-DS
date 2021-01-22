def charCount(paragraph):
    """This function accepts a text string and returns integer count of that string"""
    char_count = len(paragraph)
    return char_count


def word_count(paragraph):
    """This function accepts a text string and returns integer count of word"""
    word_count = len(paragraph.split(" "))
    return word_count
    
    