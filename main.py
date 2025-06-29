from keep_alive import keep_alive
keep_alive()

import nest_asyncio
import asyncio
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

nest_asyncio.apply()

# ✅ توكن بوت تليجرام
TELEGRAM_BOT_TOKEN = "8026460134:AAHSLfvQQ727Kudh9_6dJtUgdsBppPtGQeY"

# ✅ الأسئلة والردود الجاهزة
faq = {
    "من هو فريق إسناد؟": """
👥 فريق شبابي تطوعي جامعي مستقل، يضم طلابًا من مختلف الجامعات الأردنية، يعمل على تمكين الطلبة من خلال مبادرات وفعاليات ثقافية، تعليمية، وتطوعية، بروح جماعية وشغف بالتغيير الإيجابي.
""",
    "ما أهداف إسناد؟": """
🎯 أهداف فريق إسناد:

✅ تمكين الشباب الجامعي وتعزيز دورهم المجتمعي  
📚 تنظيم فعاليات ومبادرات تعليمية وثقافية وتكنولوجية  
💡 تنمية المهارات القيادية والعمل الجماعي  
🤝 تعزيز القيم الإنسانية وروح التطوع  
🔗 بناء شبكة طلابية فاعلة داخل وخارج الجامعة  
""",
    "ما رؤية إسناد؟": """
🔭 أن نكون منصة طلابية رائدة، تُخرّج جيلًا واعيًا وفعّالًا، قادرًا على إحداث أثر في مجتمعه من خلال الفكر، المهارة، والمسؤولية.
""",
    "كيف أنضم إلى إسناد؟": """
🙋‍♂️ ببساطة، عبّئ نموذج التطوع عبر الرابط التالي:
🔗 https://docs.google.com/forms/d/e/1FAIpQLSdtvLb8V83I55Ih7WGo90OYsxmowfqLtvzMoucaJIHiDOurhQ/viewform
""",
    "ما هو رابط المجتمع؟": """
📲 انضم الآن لمجتمع إسناد على واتساب 👇
https://chat.whatsapp.com/E16b4cKa2sx4OcO4CJg2xX?mode=r_t
""",
    "من القائمون على إسناد؟": """
👨‍💼 يقود الفريق مجموعة من الطلبة المتطوعين من مختلف الكليات، بإشراف منسقين أكفاء، ويتم تنظيم العمل عبر لجان:
🧠 لجنة التخطيط  
🎨 لجنة التصميم  
📢 لجنة الإعلام  
🤖 لجنة التكنولوجيا  
🎤 لجنة الأنشطة والعلاقات  
""",
    "ما هو موقع إسناد؟": """
🌐 موقع فريق إسناد الإلكتروني:
https://esnaadteam.github.io/esnaad/
""",
    "تواصل مع الفريق": """
📱 واتساب: 0770495848  
📧 الإيميل: esnaadteamjo@gmail.com  
📸 إنستغرام: @esnaad__team  
"""
}

# ✅ زر منيو
keyboard = [[key] for key in faq.keys()]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# ✅ رد تلقائي على الرسائل
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = update.message.text
    answer = faq.get(question, "❓ السؤال غير موجود، اختر من القائمة 👇")
    await update.message.reply_text(answer, reply_markup=reply_markup)

# ✅ رسالة البدء
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 أهلًا بك في بوت فريق إسناد. اختر سؤال من القائمة 👇", reply_markup=reply_markup)

# ✅ تشغيل البوت
async def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ البوت شغال! جربه من تليجرام الآن.")
    await app.run_polling()

# ✅ ابدأ التنفيذ
asyncio.get_event_loop().run_until_complete(main())
