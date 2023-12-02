# from replit import clear
from art import logo
# HINT: You can call clear() to clear the output in the console.
# welcome commit plus logo
print(logo)
print("Welcomre to the secret auction program.\n")
# first  the all inputs
dict = []


def createDic(name, bid):
    dict.append({"name": name, "bid": bid})


def resultF(dict):
    diy = {"name": "----", "bid": 0}
    for item in range(len(dict)):
        if dict[item]["bid"] > diy["bid"]:
            diy = dict[item]
    print(f"The winner is {diy['name']} with a bid ${diy['bid']}")


cuntinoe = True
while cuntinoe:
    name = input("What is your name?: ")
    bid = int(input("What's yout bid?: $"))
    ask = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    createDic(name, bid)
    if ask == "no":
        resultF(dict)
        cuntinoe = False
