import requests
from sys import stdout, argv


token = ""
mainurl = "https://api.telegram.org/bot" + token
chat_id = "@mamkame_news"


def sendMessage(text, chat):
    response = requests.post(mainurl + '/sendMessage?chat_id=' +
                             chat_id + '&text=' + text)
    return response


if argv[1] == "-c":
    # Comment notifying
    author = ""
    for i in range(3, len(argv)):
        author += argv[i]
    test = "На мамцы новы камэнтар ад" + author + "! Давайце прачытаем.\n\
            \nЧытаць: " + str(argv[2])
else:
    # Post notifying
    test = "Новы пост на Мамцы з назовам: "
    for i in range(3, len(argv)):
        test += str(argv[i]) + " "
    test += "\n\n"
    test += "Чытаць цалкам: " + str(argv[2])

stdout.write(str(sendMessage(test, chat_id)))
