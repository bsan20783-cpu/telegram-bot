from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

TOKEN = "8992133924:AAGBoSE1r5Z3N5e5UPMUOEXsc72zQYoCwf0"

BIO = """
👤 الاسم:
بكري محمد علي عبدالغفار

🎓 التخصص:
علوم الحاسوب (IT)

🛠️ المهارات:
• حلول مشاكل السوشيال ميديا
• تقنيات الإنترنت
• علوم الحاسوب
"""

keyboard = [
    [InlineKeyboardButton("👤 نبذة عني", callback_data="about")],
    [InlineKeyboardButton("🛠️ مهاراتي", callback_data="skills")],
    [InlineKeyboardButton("📞 تواصل معي", callback_data="contact")],
    [InlineKeyboardButton("ℹ️ معلومات البوت", callback_data="info")]
]

reply_markup = InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = "https://t.me/Beko123_San/s/2"  # ضع رابط صورتك

    await update.message.reply_photo(
        photo=photo,
        caption="""
👋 مرحباً بك في البوت الشخصي

أنا بكري محمد علي عبدالغفار

استخدم الأزرار أدناه للتعرف علي أكثر.
""",
        reply_markup=reply_markup
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "about":
        await query.edit_message_caption(
            caption=f"👤 نبذة عني\n\n{BIO}",
            reply_markup=reply_markup
        )

    elif query.data == "skills":
        await query.edit_message_caption(
            caption="""
🛠️ مهاراتي

✅ حلول مشاكل السوشيال ميديا
✅ تقنيات الإنترنت
✅ علوم الحاسوب
✅ Python
✅ بوتات تيليجرام
""",
            reply_markup=reply_markup
        )

    elif query.data == "contact":
        await query.edit_message_caption(
            caption="""
📞 التواصل

WhatsApp:
+249998311726

Instagram:
@bekosan249
""",
            reply_markup=reply_markup
        )

    elif query.data == "info":
        await query.edit_message_caption(
            caption="""
ℹ️ معلومات البوت

👨‍💻 المطور:
بكري محمد علي عبدالغفار

📚 التخصص:
علوم الحاسوب (IT)

🐍 لغة البرمجة:
Python
""",
            reply_markup=reply_markup
        )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("🤖 Bot is running...")
app.run_polling()
