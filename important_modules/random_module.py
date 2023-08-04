import random

ran_num = random.random()
print(ran_num)

int_r = random.randint(40, 70)
print(int_r)

x = random.randrange(20,200,10)
print(x)

fruits = ["mango", "apple", "grapes", "kiwi", "chickoo", "guava"]

random_fruit = random.choice(fruits)
print(random_fruit)

f_names = ["sudbhod", "swapnil", "sachin", "vijay", "komal", "mamta"]
l_names = ["choudhary", "wadhankar", "kharat", "more"]
domains = ["gmail.com", "ymail.com", "outlook.com"]
symbols = ["$", "_", ".", "^", "%", "!"]

fake_emails = []
for _ in range(0,100):
    fake_emails.append(f"{random.choice(f_names)}{random.choice(symbols)}{random.choice(l_names)}@{random.choice(domains)}")

# print(fake_emails)
# for email in fake_emails:
#     if fake_emails.count(email) > 1:
#         print(email)
#
#
# rep_email = [email for email in fake_emails if fake_emails.count(email)>1]
# print(len(rep_email))

spade = list(range(1,14))
diamond = list(range(1,14))
heart = list(range(1,14))
chidi = list(range(1,14))

cards = spade+diamond+heart+chidi
# print(cards)

cards_set_1 = random.choices(cards, k=13)
cards_set_2 = random.choices(cards, k=13)
print(cards_set_1)
print(cards_set_2)


d = random.uniform(10,30)
print(d)

discount = (1000*d)/100
print(discount)