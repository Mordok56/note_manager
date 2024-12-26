note_name = input("Введите имя заметки:")
note_content = input("Введите содержание заметки:")
note_status = input("Введите статус заметки \
(пример waiting, ready, in progress):")
note_created_date = float(input("Введите дату создания заметки - дд.мм:"))
note_change_date = float(input("Введите дату изменения заметки - дд.мм:"))
header_one = input("Введите название 1 заголовка заметки: ")
header_two = input("Введите название 2 заголовка заметки: ")
note_header = [header_one, header_two]
note = {"name": note_name, "content": note_content, "status": note_status,
        "created_date": note_created_date, "change_date": note_change_date,
        "titles": note_header}  # Использование списка как ключ titles
print("Заметка")
print(f"  Имя: {note['name']}")
print(f"  Содержание: {note['content']}")
print(f"  Статус: {note['status']}")
print(f"  Дата создания: {note['created_date']}")
print(f"  Дата изменения: {note['change_date']}")
print(f"  Заголовки: {note['titles']}")
