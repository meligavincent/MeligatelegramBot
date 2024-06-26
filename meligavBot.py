from typing import Final
from telegram import Update
from telegram.ext import Application , CommandHandler , MessageHandler, filters , ContextTypes

TOKEN:Final = '7204399678:AAHVd9_PBYPMl9potLXZI96c_tJp24o6tF4'
UserName : Final = '@MeligaVBot'


async def start_command(update:Update , context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('''Welcome my friend. we will grow here together.I\'m MeligaVbot and I\'m here to help you grow mentally and spiritually. are you ready for the journey?''')
    

async def help_command(update:Update , context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('''I\'m here to help. aske me for something''')
    
async def custom_command(update:Update , context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('''Welcome to the first step to become 
                                    the man you alway want to be.''')
    
# response
def handle_response(text:str)->str:
    text = text.lower()
    if 'hello' in text:
        return 'Hey! I\'m MeligaVbot and I\'m here to help you grow mentally and spiritually. are you ready for the journey?'
    
    if 'yes' in text:
        return 'Welcome to the first step to become the man you always want to be.What do you like the most? films? series? podcast or books? '
    
    if  "films" in text:
        
        return "Try this film: Wolf of wall street , The founder"
    
    if "series" in text:
        print('senbon')
        return "Trys these series : startup ,  spotify, billions, The crown"
    
    if "books"  in text:
        return "Try these books : The miracle morning , Rich Father Poor Father , The seven habits of winners"
    
    return '''I\'m not understanding. please try to reformulate'''

async def handle_message(update:Update,context: ContextTypes.DEFAULT_TYPE):
    message_type:str  = update.message.chat.type
    text:str = update.message.text

    print(f"User ({update.message.chat.id}) in {message_type}: '{text}'")

    if message_type == 'group':
        if UserName in text:
            new_text: str = text.replace(UserName,'').strip()
            response: str = handle_response(new_text)

        else :
            return
    else:
        response:str = handle_response(text)

    print('Here is the text :',text)
    print('Bot : ',response)

    await update.message.reply_text(response)


async def error(update:Update,context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    #Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')

    app.run_polling(poll_interval=5)



