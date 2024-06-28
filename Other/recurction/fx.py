with open('abc.txt', 'r') as f:
    char_freq = {}
    for l in f.read():
        if l in char_freq:
            char_freq[l] += 1
        else:
            char_freq[l] = 1

for char, freq in char_freq.items():
    print(f"Character '{char}' appears {freq} times.")
