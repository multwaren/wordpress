import psycopg2

def insert_data():
    try:
        # PostgreSQL'e bağlanma
        conn = psycopg2.connect(
            dbname="mydatabase",
            user="db_user",
            password="db_password",
            host="postgres", 
            port="5432"
        )
        
        cursor = conn.cursor()
        
        # Veri ekleme komutu
        cursor.execute("INSERT INTO ozgur (column1, column2) VALUES ('sample_data1', 'sample_data2');")
        conn.commit()
        
        print("Veri PostgreSQL'e başarıyla eklendi.")
    
    except Exception as e:
        print(f"Veri eklerken hata oluştu: {e}")
    
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    insert_data()

