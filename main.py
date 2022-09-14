from passlib.context import CryptContext
import psycopg2


def updateadminpass(hashedpass):
    dbname = input("Nombre de la DB: ")
    user = input("Usuario (postgres): ") or "postgres"
    userid = input("Id de usuario en la db (default 2): ") or "2"
    passw = input("Contraseña: ")
    conn = psycopg2.connect(
        host="localhost",
        database=dbname,
        user=user,
        password=passw)
    cursor = conn.cursor()
    sql = "UPDATE res_users SET password='" + hashedpass +"' WHERE id=" + userid + ";"
    cursor.execute(sql)
    sql2 = "SELECT login FROM res_users WHERE id=%s" % (userid)
    cursor.execute(sql2)
    result = cursor.fetchall()
    for l in result:
        print(l[0])
    conn.commit()
    cursor.close()
    conn.close()


def hashpasswd():
    newpass = input("Nueva contraseña: ")
    setpw = CryptContext(schemes=['pbkdf2_sha512'])
    return setpw.hash(newpass)


if __name__ == '__main__':
    # print(hashpasswd())
    updateadminpass(hashpasswd())
