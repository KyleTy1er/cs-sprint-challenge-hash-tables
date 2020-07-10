#  Hint:  You may not need all of these.  Remove the unused functions.

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    """

    ticket_1 = Ticket("PIT", "ORD")
    ticket_2 = Ticket("XNA", "SAP")
    ticket_3 = Ticket("SFO", "BHM")
    ticket_4 = Ticket("FLG", "XNA")
    ticket_5 = Ticket("NONE", "LAX")
    ticket_6 = Ticket("LAX", "SFO")
    ticket_7 = Ticket("SAP", "SLC")
    ticket_8 = Ticket("ORD", "NONE")
    ticket_9 = Ticket("SLC", "PIT")
    ticket_10 = Ticket("BHM", "FLG")


    expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP",
                    "SLC", "PIT", "ORD", "NONE"]


    A ticket is only in the correct location if the ticket behind it points forward
    to it, and the ticket in front points back...

    Ticket("LAX", "SFO")
    Ticket("SFO", "BHM")
    Ticket("BHM", "FLG")


    """
    # tickets will be an array of class objects...
    # we know the first ticket is the one with a source of None...
    # and the last ticket has a destination of None....
    ticket_list = []
    for i in range(len(tickets)):
        if tickets[i].source == None:
            ticket_list[0] = tickets[i].destination

    return ticket_list
