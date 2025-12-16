def count_strings(text_list):
    numbers = 0
    letters = 0
    for item in text_list:
        if item.isdigit():
            numbers = numbers + 1
        elif item.isalpha():
            letters = letters + 1
            return(numbers , letters)
text_list = ["Hello1234567890"]
print(count_strings(text_list))