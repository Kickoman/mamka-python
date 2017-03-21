import requests
from sys import stdout, argv
import random


token = ""
mainurl = "https://api.telegram.org/bot" + token
chat_id = "@mamkame_news"

comment_news = ["На мамцы новы камэнтар ад {author}! Давайце прачытаем\n\nЧытаць: {postlink}",
                "Воў, воў, воў, што ж гэта адбываецца?! {author} кажа такія рэчы проста тут: {postlink}",
                "Ці то новы срач распальваецца? Хадзі, спраўдзь што там {author} напісаў на {postlink}"]

post_news = ["Новы пост на Мамцы з назовам: {title}\n\nЧытаць цалкам: {postlink}",
             "Бабах! Новы запіс. Можа быць, ён пра цябе? Хадзі, дазнайся, што значыць\"{title}\" на {postlink}",
             "Забыліся на мамку? А мы пра вашу - не. Чытаць {title} цалкам: {postlink}"]


def sendMessage(text, chat):
    response = requests.post(mainurl + '/sendMessage?chat_id=' +
                             chat_id + '&text=' + text)
    return response


if argv[1] == "-c":
    # Comment notifying
    author = ""
    for i in range(3, len(argv)):
        author += str(argv[i]) + " "

    test = comment_news[random.randint(0,
                                       len(comment_news) - 1)].format(author=author,
                                                                      postlink=str(argv[2]))
    # test = "На мамцы новы камэнтар ад " + author + "! Давайце прачытаем.\n\
    #         \nЧытаць: " + str(argv[2])
else:
    # Post notifying
    # test = "Новы пост на Мамцы з назовам: "
    title = ""
    for i in range(3, len(argv)):
        title += str(argv[i]) + " "
    test = post_news[random.randint(0,
                                    len(post_news) - 1)].format(title=title,
                                                                postlink=str(argv[2]))
    # test += "\n\n"
    # test += "Чытаць цалкам: " + str(argv[2])

stdout.write(str(sendMessage(test, chat_id)))
