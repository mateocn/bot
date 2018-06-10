#_*_ coding: utf-8 _*_
#Importamos la  librería
import telebot
"""Creamos una instancia de la clase telebot,
  podemos ver el API de nuestro bot 
"""
botPythonUIO = telebot.TeleBot("Token")
@botPythonUIO.message_handler(commands=['start','help'])
def send_welcome(message):
    chatID=message.chat.id
    nombreUsuario=message.chat.first_name + ''+message.chat.last_name
    saludo = "Hola {nombre}, bienvenido a nuestro bot"
    botPythonUIO.send_message(chatID,saludo.format(nombre = nombreUsuario))
print("El bot se esta ejecutando")
botPythonUIO.polling()