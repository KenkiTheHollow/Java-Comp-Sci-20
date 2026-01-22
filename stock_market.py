import random

class StockMarket:
    money = 10000.0


def display(day,
            fb_price, fb_shares,
            g_price, g_shares,
            ms_price, ms_shares,
            ts_price, ts_shares):

    total_value = (fb_price * fb_shares +
                   g_price * g_shares +
                   ms_price * ms_shares +
                   ts_price * ts_shares)

    print("\nDay", day)
    print("Company Name      Price     Shares Owned")
    print("==========================================")
    print("1. Facebook      $", round(fb_price, 2), "   ", fb_shares)
    print("2. Google        $", round(g_price, 2), "  ", g_shares)
    print("3. Microsoft     $", round(ms_price, 2), "   ", ms_shares)
    print("4. Tesla         $", round(ts_price, 2), "   ", ts_shares)
    print("Total value of all shares: $", round(total_value, 2))
    print("Total cash on hand: $", round(StockMarket.money, 2))


def updatePrice(price):
    roll = random.randint(1, 100)

    if roll <= 80:
        change = random.uniform(0.5, 3)
    elif roll <= 95:
        change = 0
    else:
        change = random.uniform(5, 15)

    direction = random.randint(0, 1)

    if direction == 0:
        price -= price * (change / 100)
    else:
        price += price * (change / 100)

    if price < 0.01:
        price = 0.01

    return price


def purchase(shares, price):
    cost = shares * price
    if cost > StockMarket.money:
        shares = int(StockMarket.money // price)
        cost = shares * price

    StockMarket.money -= cost
    return shares


def sell(shares, price):
    revenue = shares * price
    fee = revenue * 0.01
    StockMarket.money += (revenue - fee)
    return shares


def main():
    day = 1

    fb_price = 180
    g_price = 1285
    ms_price = 161
    ts_price = 702

    fb_shares = 0
    g_shares = 0
    ms_shares = 0
    ts_shares = 0

    running = True

    while running:
        display(day,
                fb_price, fb_shares,
                g_price, g_shares,
                ms_price, ms_shares,
                ts_price, ts_shares)

        print("1. Buy")
        print("2. Sell")
        print("3. End the day")
        choice = int(input("What would you like to do? "))

        if choice == 1:
            stock = int(input("Which stock would you like to buy (1-4)? "))
            amount = int(input("How many would you like to buy? "))

            if stock == 1:
                fb_shares += purchase(amount, fb_price)
            elif stock == 2:
                g_shares += purchase(amount, g_price)
            elif stock == 3:
                ms_shares += purchase(amount, ms_price)
            elif stock == 4:
                ts_shares += purchase(amount, ts_price)

        elif choice == 2:
            stock = int(input("Which stock would you like to sell (1-4)? "))
            amount = int(input("How many would you like to sell? "))

            if stock == 1 and amount <= fb_shares:
                fb_shares -= amount
                sell(amount, fb_price)
            elif stock == 2 and amount <= g_shares:
                g_shares -= amount
                sell(amount, g_price)
            elif stock == 3 and amount <= ms_shares:
                ms_shares -= amount
                sell(amount, ms_price)
            elif stock == 4 and amount <= ts_shares:
                ts_shares -= amount
                sell(amount, ts_price)

        elif choice == 3:
            day += 1
            fb_price = updatePrice(fb_price)
            g_price = updatePrice(g_price)
            ms_price = updatePrice(ms_price)
            ts_price = updatePrice(ts_price)

        if day > 365:
            running = False

        if (fb_shares + g_shares + ms_shares + ts_shares) == 0 and StockMarket.money < 100:
            running = False

    print("\nSimulation Ended")


main()
