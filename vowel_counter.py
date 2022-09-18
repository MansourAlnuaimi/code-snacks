in_text = (input("Enter text:  "))
vowel_count, j = 0, 0
a, e, i, o, u = 0, 0, 0, 0, 0
for j in range(len(in_text)):
    if in_text[j] == 'a' or in_text[j] == 'e' or in_text[j] == 'i' \
    or in_text[j] == 'o' or in_text[j] == 'u':
        vowel_count = vowel_count + 1
        if in_text[j] == 'a': a = a + 1 
        elif in_text[j] == 'e': e = e + 1
        elif in_text[j] == 'i': i = i + 1
        elif in_text[j] == 'o': o = o + 1
        elif in_text[j] == 'u': u = u + 1
print(f"\nThere are {vowel_count} vowels in your text;\n a: {a} \
        \n e: {e} \n i: {i} \n o: {o} \n u: {u}")
