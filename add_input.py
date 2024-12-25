# Программа
username = str(input("Введите имя пользователя (пример Alex):"))
title = str(input("Введите заголовок заметки (пример home_work):"))
content = str(input("Введите описание заметки (пример download_new_code):"))
status = str(input("Введите статус заметки (пример waiting, ready, in progress):"))
temp_created_date = float(input("Введите дату создания заметки - дд.мм.гг:"))
temp_issue_date = float(input("Введите дату истечения заметки - дд.мм.гг:"))
print("Создана заметка пользователя", username)
