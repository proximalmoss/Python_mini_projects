str="Eeegthhdhgieieotkddimlo".lower()
letter_count={}
for letter in str:
    letter_count[letter]=letter_count.get(letter,0)+1
non_repeating_letters=[]
for letter,count in letter_count.items():
    if count==1:
        non_repeating_letters.append(letter)
print(f"non repeating letters are: {non_repeating_letters}")