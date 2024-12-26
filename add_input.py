# Программа
username = input("Введите имя пользователя (пример Alex):")
title = input("Введите заголовок заметки (пример home_work):")
content = input("Введите описание заметки (пример download_new_code):")
status = input("Введите статус заметки (пример waiting, ready, in progress):")
created_date = float(input("Введите дату создания заметки - дд.мм.гг:"))
issue_date = float(input("Введите дату истечения заметки - дд.мм.гг:"))
print("Создана заметка пользователя", username)
