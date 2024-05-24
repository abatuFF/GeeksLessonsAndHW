import sqlite3

def execute_query(query, params=None):
    try:
        conn = sqlite3.connect('exam.db')
        cur = conn.cursor()
        if params:
            cur.execute(query, params)
        else:
            cur.execute(query)
        results = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return results
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return []

def display_stores():
    query = "SELECT store_id, title FROM store"
    stores = execute_query(query)
    for store in stores:
        print(f"{store[0]}. {store[1]}")

def display_products(store_id):
    query = """
        SELECT p.title, c.title, p.unit_price, p.stock_quantity
        FROM products p
        JOIN categories c ON p.category_code = c.code
        WHERE p.store_id = ?
    """
    products = execute_query(query, (store_id,))
    for product in products:
        print(f"Название продукта: {product[0]}")
        print(f"Категория: {product[1]}")
        print(f"Цена: {product[2]}")
        print(f"Количество на складе: {product[3]}\n")

def main():
    while True:
        print("Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
        display_stores()
        store_id = input("Введите id магазина: ")
        if store_id == '0':
            break
        if store_id.isdigit():
            display_products(int(store_id))
        else:
            print("Некорректный ввод. Пожалуйста, введите числовое значение id магазина.")

if __name__ == "__main__":
    main()
