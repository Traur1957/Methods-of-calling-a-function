def send_email(message, recipient: str, *, sender="university.help@gmail.com"):  # endswith() - проверка, что строка заканчивается на что-то
    if recipient.endswith((".com", ".ru", ".net")) and sender.endswith((".com", ".ru", ".net")):
        if "@" not in recipient or "@" not in sender:  # Если знака собаки нет в одной из почт
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return  # завершает выполнение функции
    elif sender == recipient:
        print(f"Нельзя отправить письмо самому себе!")
        return
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        returne
    else:  # У кого-то почта некорректная
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
        return

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
