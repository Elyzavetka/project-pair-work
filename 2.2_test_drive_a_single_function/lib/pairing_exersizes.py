def make_snippet(input_string):
    # // We take a string as an argument 
    #// Return the firts fuve words
    #// Add "..." in the end of the more than 5 words
    words = input_string. split(" ")
    if len(words) > 5:
        first_five = words[:5]
        return_string = " ".join(first_five)
        
        return return_string + "..."
    else:
        return input_string

print(make_snippet("dlkgjh ksjdgh skdjgh skdjhg ksdjhhg ksjhfg"))