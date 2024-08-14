# def is_palindrome(s):
#     s = s.replace(" ", "").lower()
#     return s == s[::-1]

# user_input = input("Введіть рядок: ")
# if is_palindrome(user_input):
#     print(f"'{user_input}' є паліндромом.")
# else:
#     print(f"'{user_input}' не є паліндромом.")



# text = input("Введіть текст: ")
# reserved_words = input("Введіть список зарезервованих слів через кому: ").split(',')

# for word in text.split():
#     if word.lower() in reserved_words:
#         text = text.replace(word, word.upper())
# print(text)



# text = input("Введіть текст: ")
# sentences = re.split(r'[.!?]', text)
# print("Кількість речень у тексті:", len(sentences))
