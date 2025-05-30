import pprint
import sqlite3

# Підключення до бази
conn = sqlite3.connect('weapons.db')
cur = conn.cursor()

# Створення таблиці
cur.execute('''
CREATE TABLE IF NOT EXISTS weapons (
    name TEXT,
    price INTEGER,
    damage REAL,
    headshot REAL,
    alternate_damage REAL,
    alternate_headshot REAL
)
''')

# Дані зброї з None заміненим на 0
weapons_data = [
    ("Feedbacker", 0, 1, 1, 0, 0),
    ("Knuckleblaster", 0, 3.5, 3.5, 0, 0),
    ("Whiplash", 0, 0.2, 0.2, 0, 0),

    ("Piercer Revolver", 0, 1, 2, 3, 4.5 / 6),
    ("Marksman Revolver", 7500, 1, 2, 2, 2),
    ("Sharpshooter Revolver", 25000, 1, 2, 3, 6),
    ("Alternate Piercer", 0, 2.5, 5, 7.5, 12.5),
    ("Alternate Marksman", 0, 2.5, 5, 5.25, 5.25),
    ("Alternate Sharpshooter", 0, 2.5, 5, 5, 10),

    ("Core Eject Shotgun", 0, 3 * (0.25 / 12), 3 * (0.25 / 10), 3.5, 3.5),
    ("Pump Charge Shotgun", 12500, 2.5 * (0.25 / 10), 2.5 * (0.25 / 10), 4 * (0.25 / 16), 6 * (0.25 / 24)),
    ("Sawed-On Shotgun", 25000, 3 * (0.25 / 12), 3 * (0.25 / 10), 0.25 / 1.5, 0.25 / 1.5),
    ("Green Jackhammer", 0, 3, 3, 0, 0),
    ("Yellow Jackhammer", 0, 6, 6, 0, 0),
    ("Red Jackhammer", 0, 10, 10, 0, 0),

    ("Attractor Nailgun", 0, 0.205, 0.205, 0, 0),
    ("Overheat Nailgun", 25000, 2.3125 / 4.625, 2.3125 / 4.625, 11.47, 11.47),
    ("Jumpstart Nailgun", 35000, 2.96 / 4.625, 2.96 / 4.625, 10, 10),
    ("Sawblade Launcher Attractor", 0, 0.75 / 2.25, 0.75 / 2.25, 0, 0),
    ("Sawblade Launcher Overheat", 0, 0.75 / 2.25, 0.75 / 2.25, 0.75 * 0.5, 0.75 * 0.5),
    ("Sawblade Launcher JumpStart", 0, 0.75 / 2.25, 0.75 / 2.25, 0, 0),

    ("Electric Railcannon", 0, 8, 8, 0, 0),
    ("Screwdriver Railcannon", 100000, 3 / 7.25 + 5, 8, 0, 0),
    ("Malicious Railcannon", 100000, 2 + 6.25, 2 + 6.25, 0, 0),

    ("Freezeframe Rocket Launcher", 0, 0, 0, 0, 0),
    ("S.R.S. Cannon Rocket Launcher", 75000, 0, 0, 50, 50),
    ("Firestarter Rocket Launcher", 75000, 0, 0, 50, 50),
]

# Очищення старих даних
cur.execute("DELETE FROM weapons")

# Вставка нових
cur.executemany('''
INSERT INTO weapons (name, price, damage, headshot, alternate_damage, alternate_headshot)
VALUES (?, ?, ?, ?, ?, ?)
''', weapons_data)

conn.commit()
conn.close()


# Отримання даних для перевірки
def get_all_weapons():
    """
    Повертає список усієї зброї з бази даних.
    Всі поля конвертовані в текст, None або некоректні значення замінені на '0'.
    """
    conn = sqlite3.connect('weapons.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM weapons")
    rows = cursor.fetchall()
    conn.close()

    def clean_value(val):
        if val is None:
            return '0'
        # Якщо вже рядок, але він пустий або "None" - замінимо теж
        if isinstance(val, str):
            if val.strip() == '' or val.strip().lower() == 'none':
                return '0'
            return val
        # Якщо число — конвертуємо в рядок
        return str(val)

    # Конвертуємо кожен запис: усі поля — рядки, None → '0'
    cleaned_data = []
    for row in rows:
        cleaned_row = tuple(clean_value(field) for field in row)
        cleaned_data.append(cleaned_row)
    pprint.pprint(cleaned_data)
    return cleaned_data

# Вивід
for weapon in get_all_weapons():
    print(f"{weapon[0]} | Ціна: {weapon[1]} | Шкода: {weapon[2]}")
