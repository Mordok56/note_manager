note_name = str(input("Введите имя заметки:"))
note_content = str(input("Введите содержание заметки:"))
note_status = str(input("Введите статус заметки \
(пример waiting, ready, in progress):"))
note_created_date = float(input("Введите дату создания заметки - дд.мм:"))
note_change_date = float(input("Введите дату изменения заметки - дд.мм:"))
header_one = input("Введите название 1 заголовка заметки: ")
header_two = input("Введите название 2 заголовка заметки: ")
note_header = [header_one, header_two]
note = [note_name, note_content, note_status, note_created_date,
        note_change_date, note_header]
print("Заметка")
print(f"  Имя: {note_name}")
print(f"  Содержание: {note_content}")
print(f"  Статус: {note_status}")
print(f"  Дата создания: {note_created_date}")
print(f"  Дата изменения: {note_change_date}")
print(f"  Заголовки: {note_header}")
