import csv

# Пути
visit_log_file = '/mnt/data/visit_log__1___2_.csv'  # ваш загруженный файл
purchase_log_file = 'purchase_log.csv'  # файл, который нужно будет подключить, если у вас есть
output_file = '/mnt/data/funnel.csv'

# Чтение данных о покупках
purchase_dict = {}
try:
    with open(purchase_log_file, mode='r', encoding='utf-8') as purchase_file:
        reader = csv.DictReader(purchase_file)
        for row in reader:
            purchase_dict[row['user_id']] = row['category']
except FileNotFoundError:
    print("Файл purchase_log.csv не найден. Пожалуйста, добавьте файл покупок.")

# Построчная обработка
with open(visit_log_file, mode='r', encoding='utf-8') as visit_file, \
        open(output_file, mode='w', encoding='utf-8', newline='') as funnel_file:
    reader = csv.DictReader(visit_file)
    fieldnames = reader.fieldnames + ['category']  # Добавляем новый столбец "category"
    writer = csv.DictWriter(funnel_file, fieldnames=fieldnames)

    # Записываем заголовок
    writer.writeheader()

    for row in reader:
        user_id = row['user_id']
        if user_id in purchase_dict:  # Если пользователь совершал покупку
            row['category'] = purchase_dict[user_id]
            writer.writerow(row)

print(f"Файл funnel.csv успешно создан: {output_file}")