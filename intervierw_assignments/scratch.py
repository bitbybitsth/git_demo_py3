vowels = "aeiou"
st1 = "tEst**"
st1 = st1.lower()


v_c = 0
c_c = 0

for i in st1:
    if i in vowels and i.isalpha():
        v_c +=1
    elif i.isalpha():
        c_c +=1

print(v_c)
print(c_c)


s1 = "Takute has passed Maharashtra passed passed "

sub_str = "passed"
sub_str_count = 0
for i in range(len(s1)):
    if sub_str.startswith(s1[i]):
        for ind, j in enumerate(sub_str, start=i):
            if j != s1[ind]:
                break
        else:
            sub_str_count +=1

print("*****", sub_str_count)



print(len(s1.split()))
print(s1.replace(" ","*"))

#
# tup = vowel_consonant("s1")
# print(f"Vowel Count={tup[0]}, consonants count={tup[1]}")

unit = 200
range(0, 4000)

if 0 < unit < 4000:
    pass

def even_odd_sum_greater(list_of_number):
    odd_number_sum = 0
    even_number_sum = 0
    for number in list_of_number:
        if number%2==0:
            even_number_sum +=1
        else:
            odd_number_sum +=1



s = s1.split()
samllest = latgest = s[0]
samllest_len = latgest_len = len(s[0])

for word in s:
    word_len = len(word)
    if samllest_len > word_len:
        samllest = word
    if latgest_len < len(word):
        latgest = word

s1 = "te* T9"

a = d = s = 0

for letter in s1:
    if letter.isalpha():
        a+=1
    elif letter.isdigit():
        d+=1
    elif letter.isspace():
        continue
    else:
        s+=1


print(f"a={a}, d={d}, s={s}")

