import requests
import time 


def send_noTicketsFound_message():
    return requests.post(
        "https://api.mailgun.net/v3/mg.baileyberro.com/messages",
        auth=("api", "key-e2fbc66c1bedbcd47649b34cbac6df55"),
        data={"from": "TicketAutoPay <postmaster@mg.baileyberro.com>",
              "to": "Bailey <bailey@baileyberro.com>",
              "subject": "Ticket Payment For "  + time.strftime("%x"),
              "text": "Congrats! There were no tickets found!"})


def send_TicketsFound_message(numTickets, totalCost):
    return requests.post(
        "https://api.mailgun.net/v3/mg.baileyberro.com/messages",
        auth=("api", "key-e2fbc66c1bedbcd47649b34cbac6df55"),
        data={"from": "TicketAutoPay <postmaster@mg.baileyberro.com>",
              "to": "Bailey <bailey@baileyberro.com>",
              "subject": "Ticket Payment For "  + time.strftime("%x"),
              "text": "Paid " + numTickets + " tickets for a cost of " + totalCost })
