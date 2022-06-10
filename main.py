from passlib.context import CryptContext
import psycopg2


def updateadminpass(hashedpass):
    dbname = input("Nombre de la DB: ")
    user = input("Usuario (postgres): ") or "postgres"
    passw = input("Contraseña: ")
    conn = psycopg2.connect(
        host="localhost",
        database=dbname,
        user=user,
        password=passw)
    cursor = conn.cursor()
    sql = "UPDATE res_users SET password='" + hashedpass + "' WHERE id=2;"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def hashpasswd():
    newpass = input("Nueva contraseña: ")
    setpw = CryptContext(schemes=['pbkdf2_sha512'])
    return setpw.hash(newpass)


if __name__ == '__main__':
    updateadminpass(hashpasswd())
