from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # 回复使用者 /start 命令
    print('start')
    await update.message.reply_text('Hello! bot test.')

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # 回复使用者 /start 命令
    print('test')
    await update.message.reply_text('Hello! test.')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # 回复使用者 /start 命令
    print('echo')
    text = update.message.text
    await update.message.reply_text(f'You said {text}.')

def main():
    # 創建應用實例並插入你的機器人 Token
    application = Application.builder().token('6416422192:AAGE1lu4lNHEycWNRsF_oTjpySdhj7XFtx4').build()

    # 添加 /start 命令處理器
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.add_handler(CommandHandler('test', test))
    
    echo_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    application.add_handler(echo_handler)

    # 啟動機器人
    application.run_polling()

if __name__ == '__main__':
    main()