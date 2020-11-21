import random
import urllib


def random_card():
    card = ["4000056655665556", "4242424242424242", "5555555555554444", "2223003122003222", "5200828282828210",
            "378282246310005", "371449635398431", "6200000000000005", "36227206271667", "3566002020360505"]
    rcard = random.choice(card)
    if (len(rcard) == 15):
        type_card = 'american'
        cvc = '1234'
        lastdi = '****** ' + rcard[-4:]
    else:
        type_card = 'visa'
        cvc = '123'
        lastdi = '**** ' + rcard[-4:]
    lastdig = ("'" + lastdi + "'")
    return rcard, lastdig, type_card, cvc


number_card, last4dig, type_card, cvc_card = random_card()


