from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import os
import json

TOKEN = os.environ.get('TOKEN')
with open('tips.json') as f:
    data = json.load(f)

async def official_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # 回复使用者 /official_document 命令
    print('official_document')
    await update.message.reply_text(data['official_document'])

async def level_upgrade_tips(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # 回复使用者 /level_upgrade_tips 命令
    print('level_upgrade_tips')
    await update.message.reply_text(data['level_upgrade_tips'])

async def equipment_tips(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # 回复使用者 /equipment_tips 命令
    print('equipment_tips')
    await update.message.reply_text(data['equipment_tips'])

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # 回复使用者 /echo 命令
    print('echo')
    text = update.message.text
    await update.message.reply_text(f'You said {text}.')

def main():
    # 創建應用實例並插入你的機器人 Token
    application = Application.builder().token(TOKEN).build()

    # 添加 /start 命令處理器
    application.add_handler(CommandHandler('official_document', official_document))
    application.add_handler(CommandHandler('level_upgrade_tips', level_upgrade_tips))
    application.add_handler(CommandHandler('equipment_tips', equipment_tips))
    
    echo_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    application.add_handler(echo_handler)

    # 啟動機器人
    application.run_polling()

if __name__ == '__main__':
    main()