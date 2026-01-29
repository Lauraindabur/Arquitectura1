import mysql.connector

conexion= mysql.connector.connect(user= 'root',
                                  password= '000',
                                  database='usuarios',
                                  port='3306')

print(conexion) #probar que si está la conexion correcta

#-------------
def main():
    cursor = conexion.cursor()  # sirve para conectar con mySQL  
    nombre= input("Ingresa el nombre a guardar en la DB: ")
    sql=  "INSERT into nombreUsuario (nombre) VALUES (%s)"

    cursor.execute(sql, (nombre,))   #ejecuta la consutla sql e ingresa el valor de la variable nombre
    conexion.commit()

    cursor.close()  #cierra la conexion
    conexion.close()


if __name__ == "__main__":
    main()