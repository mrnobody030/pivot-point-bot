from telegram import Update, ext, Bot
from datetime import date
from main import stratigy
from time import sleep

today = date.today()

Token = '7416684076:AAFqwWTpWKtPWsrOvv-SYODKthb1QE5xU70'
bot_username = '@today_pivot_pointbot'
bot = Bot(token='7416684076:AAFqwWTpWKtPWsrOvv-SYODKthb1QE5xU70')

async def start_command(update: Update, context:ext.ContextTypes.DEFAULT_TYPE):
    while True:
        try :
            do_again = True
            symbols_for_trade = []
            while do_again == True:
                do_again = False
                file = open("data.csv","r")

                lines = file.readlines()

                table = []
                for a in lines:
                    a = a.strip().split(" ")
                    a = [i for i in a if i]
                    
                    table.append(a)
                file.close()


                file = open("data.csv","w")
                for row in table:
                    if len(row) != 1 :
                        if str(today) == row[3]:
                            file.write(row[0] +"    "+ row[1] +"    "+ row[2] +"    "+ row[3] + "\n")
                            continue
                    try:
                        P_point = stratigy(row[0])
                        if P_point[0] == True:
                            file.write(str(row[0]) + "    True    " + str(P_point[1]) + "   " + str(today) + "\n")
                            symbols_for_trade.append(row[0])
                        else:
                            file.write(str(row[0]) + "    False    no_point   " + str(today) + "\n")
                        sleep(15)
                    except ConnectionError:
                        print("please check if you are connected to the internet")
                    except :
                        do_again = True
                        file.write(str(row[0]) + "\n")
                        print("an error acured on " + row[0])
            file.close()
            if symbols_for_trade:
                await update.message.reply_text("this symbols have the condetions to trade today \n"+ " ".join(symbols_for_trade))
            sleep(60*60*24)
        except:
            await update.message.reply_text("there is an error pls come and check on it")

async def help_command(update: Update, context:ext.ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(""" This are the commaands that are available
/start - starts the bot
/help - this commend show you the commends
/today_pivot_point - gives pairs that pivot point might work on for today
""")
    

async def today_pivot_point_commend(update: Update, context:ext.ContextTypes.DEFAULT_TYPE):
    do_again = True
    symbols_for_trade = []
    while do_again == True:
        do_again = False
        file = open("data.csv","r")

        lines = file.readlines()

        table = []
        for a in lines:
            a = a.strip().split(" ")
            a = [i for i in a if i]
            
            table.append(a)
        file.close()


        file = open("data.csv","w")
        for row in table:
            if len(row) != 1 :
                if str(today) == row[3]:
                    file.write(row[0] +"    "+ row[1] +"    "+ row[2] +"    "+ row[3] + "\n")
                    continue
            try:
                P_point = stratigy(row[0])
                if P_point[0] == True:
                    file.write(str(row[0]) + "    True    " + str(P_point[1]) + "   " + str(today) + "\n")
                    symbols_for_trade.append(row[0])
                else:
                    file.write(str(row[0]) + "    False    no_point   " + str(today) + "\n")
                sleep(15)
            except ConnectionError:
                print("please check if you are connected to the internet")
            except :
                do_again = True
                file.write(str(row[0]) + "\n")
                print("an error acured on " + row[0])
    file.close()
    if symbols_for_trade:
        await update.message.reply_text("this symbols have the condetions to trade today \n"+ " ".join(symbols_for_trade))

async def test():
    await bot.send_message(chat_id=-4514419652, text="testing")

async def error(update: Update , context:ext.ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


if __name__ == '__main__':
    print("starting bot...")
    app = ext.Application.builder().token(Token).build()

    print("pulling...")
    #commands
    app.add_handler(ext.CommandHandler('start', start_command))
    app.add_handler(ext.CommandHandler('help', help_command))
    app.add_handler(ext.CommandHandler('today_pivot_point', today_pivot_point_commend))



    #error
    app.add_error_handler(error)


    app.run_polling(poll_interval=3)