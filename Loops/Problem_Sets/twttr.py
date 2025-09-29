

text = str(input("Input: "))
vowels = "aeiouAEIOU"
new_text = ""

for char in text:
    if char not in vowels:
        new_text += char
print("Output:", new_text)

