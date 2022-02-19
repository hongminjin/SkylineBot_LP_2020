import pickle
import sys
import os
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from antlr4 import *
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
from cl.SkylineLexer import SkylineLexer
from cl.SkylineParser import SkylineParser
from cl.EvalVisitor import EvalVisitor
from skyline import Skyline


# inicialitza la taula de simbols i envia missatge de benvinguda
def start(update, context):
    context.user_data['taulasimbols'] = {}
    user = update.message.chat.first_name
    txt = "SkyLineBot!\nBenvingut {}!\n".format(user)
    context.bot.send_message(chat_id=update.message.chat_id, text=txt)


# missatge d'ajuda
def t_help(update, context):
    txt = "SkyLineBot!\n" + \
          "Llista de totes les comandes:\n" + \
          "/start: inicia la conversa amb el Bot.\n" + \
          "/help: mostra una llista de totes les comandes i com funciona.\n" + \
          "/author: mostra el nom d'autor i el seu correu.\n" + \
          "/lst: mostra els identificadors definits i la seva area.\n" + \
          "/clean: esborra tots els identificadors definits.\n" + \
          "/save id: guarda el Skyline id amb el nom id.sky.\n" + \
          "/load id: carrega les informacions de l'arxiu id.sky.\n"
    context.bot.send_message(chat_id=update.message.chat_id, text=txt)


# autor
def author(update, context):
    txt = "SkyLineBot!\n" + \
          "@ Hongmin Jin 2020 \n"
    context.bot.send_message(chat_id=update.message.chat_id, text=txt)


# llista dels identificadors i la seva area
def lst(update, context):
    txt = "SkyLineBot!\nLlista dels identificadors i area:\n"
    for key, val in context.user_data['taulasimbols'].items():
        txt += "{}: {}\n".format(key, val.getArea())
    context.bot.send_message(chat_id=update.message.chat_id, text=txt)


# eliminar tots els identificadors
def clean(update, context):
    context.user_data['taulasimbols'] = {}
    txt = "SkyLineBot!\nS'ha eliminat tots els identificadors definits.\n"
    context.bot.send_message(chat_id=update.message.chat_id, text=txt)


# guardar les informacions en un fitxer
def save(update, context):
    msg = update.message.text[6:]
    txt = "SkyLineBot!\nS'ha guardat el Skyline.\n"
    taula = context.user_data['taulasimbols']
    try:
        user = update.message.from_user
        user_id = user['id']
        filename = "./{}/{}.sky".format(user_id, msg)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'wb') as file:
            pickle.dump(taula[msg], file)
    except:
        txt = "SkyLineBot!\nError al guardar les informacions.\n"
    context.bot.send_message(chat_id=update.message.chat_id, text=txt)


# llegir les informacions d'un fitxer
def load(update, context):
    msg = update.message.text[6:]
    txt = "SkyLineBot!\nS'ha carregat les informacions.\n"
    taula = context.user_data['taulasimbols']
    try:
        user = update.message.from_user
        user_id = user['id']
        filename = "./{}/{}.sky".format(user_id, msg)
        with open(filename, 'rb') as file:
            taula[msg] = pickle.load(file)
    except:
        txt = "SkyLineBot!\nError al carregar les informacions.\n"
    context.bot.send_message(chat_id=update.message.chat_id, text=txt)


# resultat d'una operacio de skylines
def skylineplot(update, context):
    try:
        msg = update.message.text
        input_stream = InputStream(msg.replace(" ", ""))
        lexer = SkylineLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = SkylineParser(token_stream)
        tree = parser.root()
        visitor = EvalVisitor(context.user_data['taulasimbols'])
        sky = visitor.visit(tree)
        edifs = sky.getEdif()
        fig = plt.figure()
        ax = fig.add_subplot(111, aspect='auto')
        plt.xlim([0, 10])
        plt.ylim([0, sky.getAlcada()+1])
        patches = []
        if len(edifs) != 0:
            plt.xlim([edifs[0][0]-1, edifs[len(edifs)-1][2]+1])
            for xmin, alc, xmax in edifs:
                patches.append(matplotlib.patches.Rectangle((xmin, 0), xmax-xmin, alc))
        ax.add_collection(PatchCollection(patches))
        fig.savefig('./tmp.png')
        plt.close(fig)
        context.bot.send_photo(chat_id=update.message.chat_id, photo=open('./tmp.png', 'rb'))
        txt = "area: {}\nalçada: {}\n".format(sky.getArea(), sky.getAlcada())
        context.bot.send_message(chat_id=update.message.chat_id, text=txt)
    except:
        txt = "SkyLineBot!\nExpressió incorrecta!\n"
        context.bot.send_message(chat_id=update.message.chat_id, text=txt)

TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', t_help))
updater.dispatcher.add_handler(CommandHandler('author', author))
updater.dispatcher.add_handler(CommandHandler('lst', lst))
updater.dispatcher.add_handler(CommandHandler('clean', clean))
updater.dispatcher.add_handler(CommandHandler('save', save))
updater.dispatcher.add_handler(CommandHandler('load', load))
updater.dispatcher.add_handler(MessageHandler(Filters.text, skylineplot))
updater.start_polling()
