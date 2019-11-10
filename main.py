import random
import threading
import time
import asyncio

import vk.py

vkToken = ''
# Сюда вставляешь свой токен (Я юзал от кейта. Получить можно тут https://vkhost.github.io )


myId =  # Здесь вводишь свой айди (прим. myId = 1)


contestTriggerList = ()  # Листик слов триггеров для уведомления о розыгрыше:
# Прим. contestTriggerList = ('розыгрыш', 'конкурс')

contestWhiteList = () # Вайтлист айди для триггеров на конкурс:
# Прим. contestWhiteList = (1, 2, 3)

startMyContestTrigger = ''  # Вводишь в кавычках команду, с которой начинается свой розыгрыш
triggerWord = '' # Триггер слово в кавычках, с маленькой буквы для удаления сообщений


