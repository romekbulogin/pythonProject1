import vk_api
from peewee import PostgresqlDatabase, Model, PrimaryKeyField, TextField
import random
import psycopg2
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
#97e96d64a13704faa9f0112540ff508d74854abb751865b0dfeed9204e4ce56a1c4c37408d1164ebdbaf5
#727a21e5aff72e263de80f9dfc135f24858365045809a8336b2ba4af19fd8d7c5bb13aafb4e20d725bccd

vk_session = vk_api.VkApi(token='727a21e5aff72e263de80f9dfc135f24858365045809a8336b2ba4af19fd8d7c5bb13aafb4e20d725bccd')
db = PostgresqlDatabase('d8k9ke2c61h3hb', host='ec2-3-228-235-79.compute-1.amazonaws.com', port='5432', user='olezekfprmlfip', password='cf1b053ec8d0bcdec4e228e724d7a3b3058feade8ecf852579639523f37a0a08')

def searchByKeyWord(quickList,lst):
    for i in quickList:
        for word in lst:
            if word.find(i):
                return word

class BaseModel(Model):
    class Meta:
        database = db


class QuestionKey(BaseModel):
    id = PrimaryKeyField(unique=True)
    question = TextField()
    answer = TextField()
    key_word = TextField()
    class Meta:
        table_name = 'QuestionKey'

try:
    db.connect()
except NameError:
    print(NameError)


def copyBase():
    questList = []
    try:
        with db:
            for quest in QuestionKey.select():
                questList.append(quest.question)
    except NameError:
        print(NameError)
    return questList

attachments = []
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
questList = copyBase()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if not questList.__contains__(event.text) and event.text!='Начать':
            keyboard = VkKeyboard(one_time=True)
            if event.from_user:
                try:
                    with db:
                        for quest in QuestionKey.select().where(QuestionKey.key_word.contains(event.text)):
                            keyboard.add_button(quest.question, VkKeyboardColor.POSITIVE)
                            keyboard.add_line()
                        keyboard.add_openlink_button('Задать вопрос','https://docs.google.com/forms/d/e/1FAIpQLSf6nh4sE13CFDrg0BUJYVxZ1LcCMTS2O2J6nIo3hle99xSXxw/viewform')
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Похожие вопросы',
                        random_id=random.randint(0, 999999999),
                        keyboard=keyboard.get_keyboard()
                    )
                    print("Text message: ", event.text, " from id: ", event.user_id)
                except Exception:
                    print(NameError)

        if questList.__contains__(event.text):
            print('work')
            keyboard = VkKeyboard(one_time=True)
            if event.from_user:
                try:
                    with db:
                        for quest in QuestionKey.select().where(QuestionKey.question.contains(event.text)):
                            vk.messages.send(
                                user_id=event.user_id,
                                message=quest.answer,
                                random_id=random.randint(0, 999999999),
                            )
                    print("Text message: ", event.text, " from id: ", event.user_id)
                except NameError:
                    print(NameError)
        if event.text == 'Начать':
            if event.from_user:
                try:
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Привет! Виртуальный наставник Макс готов ответить на любой твой вопрос',
                        random_id=random.randint(0, 999999999),
                    )
                except NameError:
                    print(NameError)
        if event.text == 'Расшифровка аудиторий':
            if event.from_user:
                try:
                    vk.messages.send(
                        user_id=event.user_id,
                        attachment='photo-213932615_457239020',
                        random_id=random.randint(0, 999999999)
                    )
                except NameError:
                    print(NameError)
        if event.text == 'Кампус на Социалистической, 162':
            if event.from_user:
                try:
                    vk.messages.send(
                        user_id=event.user_id,
                        attachment='photo-213932615_457239018',
                        random_id=random.randint(0, 999999999)
                    )
                except NameError:
                    print(NameError)
        if event.text == 'Кампус на пл.Гагарина':
            if event.from_user:
                try:
                    vk.messages.send(
                        user_id=event.user_id,
                        attachment='photo-213932615_457239019',
                        random_id=random.randint(0, 999999999)
                    )
                except NameError:
                    print(NameError)
        if event.text == 'Стипендия':
            if event.from_user:
                try:
                    vk.messages.send(
                        user_id=event.user_id,
                        attachment='photo-213932615_457239017',
                        random_id=random.randint(0, 999999999)
                    )
                except NameError:
                    print(NameError)