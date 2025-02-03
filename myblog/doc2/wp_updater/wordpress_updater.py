import pymysql
import time

def update_wordpress_post():
    connection = None  
    max_retries = 3
    retry_delay = 5 
    
    for attempt in range(max_retries):
        try:
            connection = pymysql.connect(
                host="myblog-db-1",         
                user="wordpress",
                password="wordpress",
                database="wordpress",
                charset="utf8mb4",
                cursorclass=pymysql.cursors.DictCursor
            )
            
            # Güncelleme işlemi
            with connection.cursor() as cursor:
                sql = """
                UPDATE wp_posts 
                SET 
                    post_title = 'ÖZGÜR BU YAZIYI GÜNCELLEDİ!', 
                    post_content = 'Bu yazı scriptle güncellendi ' 
                WHERE ID = 1
                """
                cursor.execute(sql)
            connection.commit()
            print(" Yazı güncellendi!")
            return #Olduysa çık

        except pymysql.MySQLError as e:  
            print(f"⏳ Deneme {attempt+1}/{max_retries}: {e}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
                continue
            print("Maksimum deneme sayısına ulaşıldı")

        finally:  
            if connection: 
                connection.close()

if __name__ == "__main__":
    update_wordpress_post()
