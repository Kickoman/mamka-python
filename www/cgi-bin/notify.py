import requests
from sys import stdout, argv


token = ""
mainurl = "https://api.telegram.org/bot" + token
chat_id = "@mamkame_news"


def sendMessage(text, chat):
    response = requests.post(mainurl + '/sendMessage?chat_id=' +
                             chat_id + '&text=' + text)
    return response


# test = "New post! Penis Benis! " + str(argv)
test = "Новы пост на Мамцы з назовам: "
for i in range(2, len(argv)):
    test += str(argv[i]) + " "
test += "\n\n"
test += "Чытаць цалкам: " + str(argv[1])

stdout.write(str(sendMessage(test, chat_id)))
