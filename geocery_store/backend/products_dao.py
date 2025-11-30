from sql_conection import get_sql_conection

def get_all_products(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM gs.prdoucts" 
    cursor.execute(query)

    response = []
    for (product_id, name, uom_id, price_per_unit) in cursor:
        response.append({
            "product_id": product_id,
            "name": name,
            "uom_id": uom_id,
            "price_per_unit": price_per_unit
        })

    cursor.close()
    return response


if __name__ == "__main__":
    connection = get_sql_conection()
    print(get_all_products(connection))
    connection.close()
