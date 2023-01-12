class Newspaper:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} - {self.price}"

    def __str__(self):
        return f"{self.name} - {self.price}"

    def __eq__(self, other):

        if isinstance(other, Newspaper):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)


class NewspaperSubscription:

    def __init__(self, budget):
        self.budget = budget
        self.newspapers = [
            Newspaper("TOI", 26),
            Newspaper("Hindu", 20.5),
            Newspaper("ET", 34),
            Newspaper("BM", 10.5),
            Newspaper("HT", 18),
        ]

    def get_subscriptions(self):
        subscriptions = []
        for newspaper in self.newspapers:
            if newspaper.price <= self.budget:
                subscriptions.append(newspaper)
        return subscriptions

    def get_subscription_combinations(self):
        subscriptions = self.get_subscriptions()
        combinations = []
        for i in range(len(subscriptions)):
            for j in range(i, len(subscriptions)):
                if subscriptions[i].price + subscriptions[j].price <= self.budget:
                    combinations.append({subscriptions[i], subscriptions[j]})
        return combinations


if __name__ == "__main__":
    budget = float(input("Enter the budget: "))
    newspaper_subscription = NewspaperSubscription(budget)
    print(newspaper_subscription.get_subscription_combinations())