import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


vk_session = vk_api.VkApi(token='727a21e5aff72e263de80f9dfc135f24858365045809a8336b2ba4af19fd8d7c5bb13aafb4e20d725bccd')

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text == 'test':
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    message='Hello,test',
                    random_id=212412
	            )

##if __name__ == '__main__':