import telebot
token = "297126393:AAFuA5sjV76CFK9NaiF913YwFD8nvpBIsSI"
classes = ['7', '8', '9']
classes_two = ['10', '11']
liters = ["А", "Б", "В", "Г", "Д"]
liters_two = ["А", "Б", "В", "Г"]
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Сегодня", "Завтра"]

classesMarkup = telebot.types.ReplyKeyboardMarkup()
classesMarkup.row('10', '11')
classesMarkup.row('7', '8', '9')
classesMarkup.row('/start')

litersMarkup = telebot.types.ReplyKeyboardMarkup()
litersMarkup.row("А", "Б", "В")
litersMarkup.row( "Г", "Д")
litersMarkup.row('/start')


liters_twoMarkup = telebot.types.ReplyKeyboardMarkup()
liters_twoMarkup.row("А", "Б")
liters_twoMarkup.row("В", "Г")
liters_twoMarkup.row('/start')


daysMarkup = telebot.types.ReplyKeyboardMarkup()
daysMarkup.row("Сегодня", "Завтра")
daysMarkup.row("Понедельник", "Вторник", "Среда")
daysMarkup.row("Четверг", "Пятница", "Суббота")
daysMarkup.row('/start')
