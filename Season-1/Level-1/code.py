'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    payments = Decimal('0')
    expenses = Decimal('0')
    MAX_AMT = 1000000
    MAX_QTY = 100
    MAX_PAY = 1e6

    for item in order.items:
        if item.type == 'payment':
            payments += Decimal(str(item.amount))
        elif item.type == 'product' and 0 <= item.amount <= MAX_AMT and 0 <= item.quantity <= MAX_QTY:
            expenses += Decimal(str(item.amount)) * int(item.quantity)
        else:
            return "Invalid item type: %s" % item.type

    if payments > MAX_PAY or expenses > MAX_PAY:
        return "Total amount payable for an order exceeded"

    if payments != expenses:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, payments - expenses)
    else:
        return "Order ID: %s - Full payment received!" % order.id