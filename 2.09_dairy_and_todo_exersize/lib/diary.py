import re
from math import ceil


class Diary():
    def __init__(self):
        self._list_of_diary_entries = []

    def add(self, diary_entry):
        self._list_of_diary_entries.append(diary_entry)

    def get_list_of_diary_entries(self):
        return self._list_of_diary_entries

    def get_diary_entry_by_the_time(self, wpm, time):
        for entry in self._list_of_diary_entries:
            count_words_in_entry = len(entry._experience.split())
            # len(self.contents.split())
            print(count_words_in_entry)
            if time >= ceil(count_words_in_entry / wpm):
                print(entry._experience)
                return entry._experience
        return 5

    def see_a_list_of_mobile_phones(self):
        phone_numbers = []
        for entry in self._list_of_diary_entries:
            phone_numbers += re.findall(r"0[0-9]{10}", entry._experience)
        return phone_numbers
