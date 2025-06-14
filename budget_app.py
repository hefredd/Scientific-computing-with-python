class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description })
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description })
            return True
        return False
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False
    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f'{self.name:*^30}\n'
        items = ""
        for item in self.ledger:
            amount = f"{item['amount']:>7.2f}"
            desc = item['description'][:23]
            items += f'{desc:<23}{amount}\n'
        total = f'Total: {self.get_balance():.2f}' 
        return title + items + total




def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    withdrawls = []
    names = []

    for category in categories:
        total = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total += -item['amount']
        withdrawls.append(total)
        names.append(category.name)

    total_spent = sum(withdrawls)
    percentages = [int((amount / total_spent *10) * 10) for amount in withdrawls]

    for i in range(100, -1, -10):
        title += f"{i:>3}| "
        for p in percentages:
            title += "o  " if p >= i else "   "
        title += "\n"

    title += "    -" + "---"* len(categories)+ "\n"
    
    max_length = max(len(name) for name in names)
    for i in range(max_length):
        title += "     "
        for name in names:
            title += (name[i] if i < len(name) else " ") + "  "
        title += "\n"

    return title.rstrip("\n")    

