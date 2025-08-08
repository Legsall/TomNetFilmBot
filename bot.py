import telebot

# Твой API токен
API_TOKEN = "8174172322:AAGs9VphZPkOfRhLCoODr5kwwOd04oqUFqg"

bot = telebot.TeleBot(API_TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 "🎬 Привет! Я — TomNetFilm, твой личный кино-помощник!\n\n"
                 "Напиши название фильма или сериала, и я пришлю тебе ссылку или прямо в бота, в хорошем качестве.")

# Команда /info
@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message,
                 "📌 Что я умею:\n\n"
                 "1️⃣ Заказать любой фильм или сериал по названию\n"
                 "2️⃣ Получить ссылку в хорошем качестве и без рекламы\n"
                 "3️⃣ Искать по жанрам, актёрам или году\n"
                 "4️⃣ Следить за новинками\n"
                 "5️⃣ Получать рекомендации\n\n"
                 "Просто напиши название — и я пришлю фильм!")

# Команда /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,
                 "Если возникли проблемы с ботом, пожалуйста, свяжитесь с админом @legsal_1:\n")

# Команда /support
@bot.message_handler(commands=['support'])
def send_support(message):
    bot.reply_to(message,
        "Привет, друзья! Если вам нравится мой контент и вы хотите поддержать мой труд,\n"
        "буду рад любой помощи. Ваша поддержка помогает развивать канал и делать еще больше интересного контента!\n\n"
        "Реквизиты:\n"
        "Карта (Мир-ЮМани): 2204120119979512 (ЮMoney)\n"
        "ЮMoney (ЮМани Кошелек): 4100118775949612"
    )


bot.reply_to(message, text)


# Команда /privacy (политика конфиденциальности)
@bot.message_handler(commands=['privacy'])
def send_privacy(message):
    bot.reply_to(message,
                 "🔒 Политика конфиденциальности TomNetFilm:\n\n"
                 "Мы не собираем и не храним ваши личные данные. Все запросы обрабатываются анонимно "
                 "и используются только для отправки вам фильмов и сериалов.")

# Запуск бота
print("✅ Бот запущен и готов к работе!")
bot.infinity_polling()
