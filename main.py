# main.py
# Asks bot owner for their token and monkey type key for the bot to function.

import bot
def main():
    TOKEN = input('Enter the TOKEN: ')
    APE_KEY = input('Enter the APE KEY: ')
    bot.run_discord_bot(TOKEN, APE_KEY)

if __name__ == '__main__':
    main()