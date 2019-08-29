import telegram

mu_token = '911030405:AAHnP1nWzM5xdHWwLqDk4fTUIjHx7upFbZg'
mu = telegram.Bot(token= mu_token)
updates = mu.getUpdates()
for u in updates:
    print(u.message)