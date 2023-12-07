import mysql.connector
import pandas as pd

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password",
    database="rpg",
    port=13306
)


cmd = db.cursor()
print(db)

cmd.execute("SHOW DATABASES")

for x in cmd:
    print(x)

cmd.execute("SHOW TABLES")

for x in cmd:
    print(x)


def print_users_characters():
    sql = """SELECT Usuario.nome AS user, Personagens.apelido AS personagem
            FROM Usuario
            INNER JOIN Personagens ON Usuario.id = Personagens.usuarioID;"""
    cmd.execute(sql)
    result = cmd.fetchall()

    for x in result:
        print(x)


def criar_usuario(usuario_data):
    sql = "INSERT INTO Usuarios (id, nome, senha, email) VALUES (%s, %s, %s, %s)"
    cmd.execute(sql, usuario_data)
    db.commit()
    print(cmd.rowcount, "inserido.")


def criar_personagem(personagem_data):
    sql = """INSERT INTO Personagens (apelido, nivel, forca, inteligencia, agilidade, vigor, inventario, classe, grupo, usuarioID)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    cmd.execute(sql, personagem_data)
    db.commit()
    print(cmd.rowcount, "inserido")


def deletar_usuario(usuario_id):
    sql = f"DELETE FROM Usuarios WHERE id = {usuario_id}"
    cmd.execute(sql)
    db.commit()
    print(cmd.rowcount, "deletado(s)")


def deletar_personagem(personagem_id, usuario_id):
    sql = f"""DELETE FROM Personagens WHERE id = {personagem_id}
            AND usuario_id = {usuario_id}"""
    cmd.execute(sql)
    db.commit()
    print(cmd.rowcount, "deletado(s)")


def dump_table_csv(table_name):
    cmd.execute(f"SELECT * FROM {table_name}")
    header = [row[0] for row in cmd.description]
    rows = cmd.fetchall()

    f = open(table_name + '.csv', 'w')

    f.write(','.join(header) + '\n')

    for row in rows:
        f.write(','.join(str(r) for r in row) + '\n')

    f.close()
    print(str(len(rows)) + 'linhas escrita(s) para: ' + f.name)


def dump_all_csv():
    cmd.execute("SHOW TABLES")
    result = cmd.fetchall()
    tables = []
    for x in result:
        test = ""
        test += ', '.join(map(str, x))
        tables.append(test)

    for e in tables:
        dump_table_csv(e)


def restore_table_from_csv(table_name):
    csv = pd.read.csv(f'{table_name}.csv')
    y = []
    for i in range(len(csv)):
        x = tuple(csv.iloc[i])
        y.append(x)

    if table_name == "Usuario":
        criar_usuario(y)
    elif table_name == "Personagens":
        criar_personagem(y)


def restore_all_from_csv():
    restore_table_from_csv("Personagens")
    restore_table_from_csv("Usuario")


print_users_characters()
dump_all_csv()
