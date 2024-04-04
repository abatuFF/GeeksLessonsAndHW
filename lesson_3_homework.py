vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

while True:
    user_input = input("Enter a word or 'exit' to quit: ")
    if user_input.lower() == 'exit':
        break

    vowel_count = 0
    consonant_count = 0

    for sym in user_input:
        if sym in vowels:
            vowel_count += 1
        elif sym in consonants:
            consonant_count += 1

    total_letters = vowel_count + consonant_count

    if total_letters == 0:
        print("No letters found.")
    else:
        vowel_percentage = (vowel_count / total_letters) * 100
        consonant_percentage = (consonant_count / total_letters) * 100
        print(f"Word: {user_input}")
        print(f"Total letters: {total_letters}")
        print(f"Vowels: {vowel_count}")
        print(f"Consonants: {consonant_count}")
        print(f"Vowels/Consonants: {vowel_percentage:.2f}% / {consonant_percentage:.2f}%")

