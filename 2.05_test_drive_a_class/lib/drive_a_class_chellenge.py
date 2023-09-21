class GrammarStats:
    def __init__(self):
        self.right_grammar = 0
        self.total_grammar = 0

    def check(self, text):
        accept_punctuation = ["!", ".", "?", ":", ";"]
        if text[0].isupper() and text[-1] in accept_punctuation:
            self.total_grammar += 1
            self.right_grammar += 1
            return True
        else:
            self.total_grammar += 1
            return False
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
    def percentage_good(self):
        return round(self.right_grammar / 1 * self.total_grammar * 100, 2)
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        