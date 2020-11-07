import random


def card_used(number):
    return "**** " % number[4:]


def randomcard():
    # card = ["4242424242424242", "4000056655665556", "5555555555554444", "2223003122003222", "5200828282828210",
    #             "378282246310005", "371449635398431", "6200000000000005"]
    card = ["4242424242424242", "4000056655665556", "5555555555554444", "2223003122003222", "5200828282828210",
                "378282246310005"]
    return random.choice(card)


def strip_slot_time(text):
    if "Arriving" in text:
        return text[8:]
    elif "Before" in text:
        return text[7:15]
    else:
        return text[:8]


def ssn_format(number):
    return number[:3]+'-'+number[3:5]+'-'+number[5:]


def dob_format(number):
    return number[:2]+'/'+number[2:4]+'/'+number[4:]
# def return_value_from_map(list):
#    aux = []
#    for item in list:
#        aux.append(symptoms_values.get(item))
#    return_value_from_map(aux)