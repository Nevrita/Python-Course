class ReverseString:
    def __init__(self, s):
        self.s = s

    def get_reversed(self):
        return self.s[::-1]

word = input("Enter a word: ")

reverser = ReverseString(word)
print("Reversed word:", reverser.get_reversed())