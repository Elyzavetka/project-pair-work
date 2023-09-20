#//problem - check that the first word is capitalized and after the last we have a proper punctuation
#//signature - verify_punctuation. Argument: one input string. Output: boolean.
#//tests - "Right punctuation." "wrong punctuation"
#//implement - check [0] index it's capitalize and [-1] last index. And return True, if both True.


def verify_punctuation(input_string):
    accept_punctuation = ["!", ".", "?", ":", ";"]
    if input_string[0].isupper() and input_string[-1] in accept_punctuation:
        return True
    else:
        return False
