#// We need to know how long it's takes to read some text
#//problem - estimate time reading
#//signature - estimated_time_to_read. Arguments: input_str. Return: int
#//tests - Any string >> time
#//implement behaviour - 1.We will count how many words in the string. 2. We will calculate how much time it takes for read one word. 3. Multiply count of words on speed which need for reading one word.
def estimated_time_to_read(input_str):
    words = len(input_str.split(" "))
    time_for_one_word = 1/200
    result_time = words * time_for_one_word
    return result_time

