# Тестовый ввод переменных
created_date = "11.11.2024"
issue_date = "12.12.2024"
# Программа
temp_created_date = float(created_date[:-5])
temp_issue_date = float(issue_date[:-5])
print("День-Месяц-Год:", temp_created_date)  # (дата создания заметки)
print("День-Месяц-Год:", temp_issue_date)  # (дата истечения заметки - Дедлайн)
