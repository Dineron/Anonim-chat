import telebot
from telebot import types
import pyautogui as GUI
 
Data = "Uid.txt"
 
bot = telebot.TeleBot("TOKAAAn")
 
@bot.message_handler(commands=['RegisterProfile'])
def send(message):
    RFile = open(Data, "r")
    controller = False
    for el in RFile.read().split("\n"):
        if el == str(message.chat.id):
            controller = True
    RFile.close()
    if controller == False:
        WFile = open(Data, "a")
        WFile.write(str(message.chat.id) + "\n")
        WFile.close()
        bot.send_message(message.chat.id, "Ви успішно зарегеструвались, можете починати бесіду")
    else:
        bot.send_message(message.chat.id, "ВИ ВЖЕ ЗАРЕГЕСТРУВАЛИСЬ")


@bot.message_handler(commands=['Exit'])
def send(message):
    fileR = open(Data, "r")
    FileR1 = fileR.read().split("\n")
    fileR.close()
    for el in FileR1:
        if el == str(message.chat.id):
            print(el)            
            FileR1.remove(el)
        print(FileR1)
        fileW = open(Data, "w")
        fileW.write("\n".join(FileR1) + "\n")





    # RFile = open(Data, "r")
    # controller = False
    # for el in RFile.read().split("\n"):
    #     if el == str(message.chat.id):
    #         controller = True
    #     else : pass
    
    # if controller == True:
    #     WFile = open(Data, "a")

    #     # RFile.read().replace(str(message.chat.id), "")
    #      RFile.read().replace(message.chat.id, "")
    #     WFile.close()
    #     bot.send_message(message.chat.id, "Ви успішно покинули бесіду")
    # else:
    #     bot.send_message(message.chat.id, "ВИ ВЖЕ НЕ ЗАРЕГЕСТРОВАНІ")
    # RFile.close()      





@bot.message_handler(content_types=["text"])
def text(message):

    file = open(Data, "r")
    UserId = file.read()
    file.close()
    CallData = UserId.split("\n")

    if message.chat.username == None:
        print(message.chat.id, ": " + message.from_user.first_name + "   #Текст")
    else:
        print(message.chat.id, ": " + "@" + message.from_user.username + "   #Текст")

    controller = False
    for el in CallData:
        if el == str(message.chat.id):
            controller = True
    if controller == False:
        bot.send_message(message.chat.id, "Зарегеструйтесь (/RegisterProfile)")
        return
    #CallData.remove("")

    try:
        bot.delete_message(message.chat.id, message.message_id)
    except Exception:
        pass

    for i in CallData:
        try:
            bot.send_message(i, message.from_user.first_name + ": " + message.text)
        except Exception:
            pass


@bot.message_handler(content_types=["photo"])
def photo(message):

    file = open(Data, "r")
    UserId = file.read()
    file.close()
    CallData = UserId.split("\n")

    if message.chat.username == None:
        print(message.chat.id, ": " + message.from_user.first_name + "   #фото")
    else:
        print(message.chat.id, ": " + "@" + message.from_user.username + "   #Фото")

    controller = False
    for el in CallData:
        if el == str(message.chat.id):
            controller = True
    if controller == False:
        bot.send_message(message.chat.id, "Зарегеструйтесь (/RegisterProfile)")
        return
    CallData.remove("")
    
    try:
        bot.delete_message(message.chat.id, message.message_id)
    except Exception:
        pass

    for i in CallData:
        try:
            if message.caption == None :
                bot.send_photo(i, message.photo[0].file_id, caption=(message.from_user.first_name + " : "))
            else :
                bot.send_photo(i, message.photo[0].file_id, caption=(message.from_user.first_name + " : " + message.caption))
        except Exception:
            pass

@bot.message_handler(content_types=["document"])
def text(message):

    file = open(Data, "r")
    UserId = file.read()
    file.close()
    CallData = UserId.split("\n")

    if message.chat.username == None:
        print(message.chat.id, ": " + message.from_user.first_name + "   #Документ")
    else:
        print(message.chat.id, ": " + "@" + message.from_user.username + "   #Документ")

    controller = False
    for el in CallData:
        if el == str(message.chat.id):
            controller = True
    if controller == False:
        bot.send_message(message.chat.id, "Зарегеструйтесь (/RegisterProfile)")
        return
    CallData.remove("")

    try:
        bot.delete_message(message.chat.id, message.message_id)
    except Exception:
        pass

    for i in CallData:
        try:
            if message.caption == None :
                bot.send_document(i,message.document.file_id, caption=(message.from_user.first_name + " : "))
            else :
                bot.send_document(i,message.document.file_id, caption=(message.from_user.first_name + " : " + message.caption))
        except Exception:
            pass

@bot.message_handler(content_types=["voice"])
def voice(message):

    file = open(Data, "r")
    UserId = file.read()
    file.close()
    CallData = UserId.split("\n")

    if message.chat.username == None:
        print(message.chat.id, ": " + message.from_user.first_name + "   #Войс")
    else:
        print(message.chat.id, ": " + "@" + message.from_user.username + "   #Войс")

    controller = False
    for el in CallData:
        if el == str(message.chat.id):
            controller = True
    if controller == False:
        bot.send_message(message.chat.id, "Зарегеструйтесь (/RegisterProfile)")
        return
    CallData.remove("")

    try:
        bot.delete_message(message.chat.id, message.message_id)
    except Exception:
        pass

    for i in CallData:
        try:
            if message.caption == None :
                bot.send_voice(i, message.voice.file_id, caption=(message.from_user.first_name + " : "))
            else :
                bot.send_voice(i, message.voice.file_id, caption=(message.from_user.first_name + " : " + message. caption))
        except Exception:
            pass

@bot.message_handler(content_types=["audio"])
def audio(message):

    file = open(Data, "r")
    UserId = file.read()
    file.close()
    CallData = UserId.split("\n")

    if message.chat.username == None:
        print(message.chat.id, ": " + message.from_user.first_name + "   #Аудіо")
    else:
        print(message.chat.id, ": " + "@" + message.from_user.username + "   #Аудіо")

    controller = False
    for el in CallData:
        if el == str(message.chat.id):
            controller = True
    if controller == False:
        bot.send_message(message.chat.id, "Зарегеструйтесь (/RegisterProfile)")
        return
    CallData.remove("")

    try:
        bot.delete_message(message.chat.id, message.message_id)
    except Exception:
        pass

    for i in CallData:
        try:
            if message.caption == None :
                bot.send_audio(i, message.audio.file_id, caption=(message.from_user.first_name + " : "))
            else :
                bot.send_audio(i, message.audio.file_id, caption=(message.from_user.first_name + " : " + message.caption))
        except Exception:
            pass

@bot.message_handler(content_types=["video"])
def video(message):

    file = open(Data, "r")
    UserId = file.read()
    file.close()
    CallData = UserId.split("\n")

    if message.chat.username == None:
        print(message.chat.id, ": " + message.from_user.first_name + "   #Відео")
    else:
        print(message.chat.id, ": " + "@" + message.from_user.username + "   #Відео")

    controller = False
    for el in CallData:
        if el == str(message.chat.id):
            controller = True
    if controller == False:
        bot.send_message(message.chat.id, "Зарегеструйтесь (/RegisterProfile)")
        return
    CallData.remove("")

    try:
        bot.delete_message(message.chat.id, message.message_id)
    except Exception:
        pass

    for i in CallData:
        try:
            if message.caption == None :
                bot.send_video(i, message.video.file_id, caption=(message.from_user.first_name + " : "))
            else:
                bot.send_video(i, message.video.file_id, caption=(message.from_user.first_name + " : " + message.caption))
        except Exception:
            pass

@bot.message_handler(content_types=["video_note"])
def video_note(message):

    file = open(Data, "r")
    UserId = file.read()
    file.close()
    CallData = UserId.split("\n")

    if message.chat.username == None:
        print(message.chat.id, ": " + message.from_user.first_name + "   #Кружочок")
    else:
        print(message.chat.id, ": " + "@" + message.from_user.username + "   #Кружочок")

    controller = False
    for el in CallData:
        if el == str(message.chat.id):
            controller = True
    if controller == False:
        bot.send_message(message.chat.id, "Зарегеструйтесь (/RegisterProfile)")
        return
    CallData.remove("")

    try:
        bot.delete_message(message.chat.id, message.message_id)
    except Exception:
        pass

    for i in CallData:
        try:
            if message.caption == None :
                bot.send_video(i, message.video_note.file_id, caption=(message.from_user.first_name + " : "))
            else : 
                bot.send_video(i, message.video_note.file_id, caption=(message.from_user.first_name + " : " + message.caption))
        except Exception:
            pass

@bot.message_handler(content_types=["sticker"])
def sticker(message):

    file = open(Data, "r")
    UserId = file.read()
    file.close()
    CallData = UserId.split("\n")

    if message.chat.username == None:
        print(message.chat.id, ": " + message.from_user.first_name + "   #Стікер")
    else:
        print(message.chat.id, ": " + "@" + message.from_user.username + "   #Стікер")

    controller = False
    for el in CallData:
        if el == str(message.chat.id):
            controller = True
    if controller == False:
        bot.send_message(message.chat.id, "Зарегеструйтесь (/RegisterProfile)")
        return
    CallData.remove("")

    try:
        bot.delete_message(message.chat.id, message.message_id)
    except Exception:
        pass

    for i in CallData:
        try:
            bot.send_message(i, message.from_user.first_name + " : ")
            bot.send_sticker(i, message.sticker.file_id)
        except Exception:
            pass

@bot.message_handler(content_types=["animation"])
def animation(message):

    file = open(Data, "r")
    UserId = file.read()
    file.close()
    CallData = UserId.split("\n")

    if message.chat.username == None:
        print(message.chat.id, ": " + message.from_user.first_name + "   #Гіфка")
    else:
        print(message.chat.id, ": " + "@" + message.from_user.username + "   #Гіфка")

    controller = False
    for el in CallData:
        if el == str(message.chat.id):
            controller = True
    if controller == False:
        bot.send_message(message.chat.id, "Зарегеструйтесь (/RegisterProfile)")
        return
    CallData.remove("")

    try:
        bot.delete_message(message.chat.id, message.message_id)
    except Exception:
        pass

    for i in CallData:
        try:
            bot.send_message(i, message.from_user.first_name + " : ")
            bot.send_animation(i, message.animation.file_id)
        except Exception:
            pass



bot.polling(True)