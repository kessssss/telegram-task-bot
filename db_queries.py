def db_take_all(connection, user_id):
    cursor = connection.cursor()
    cursor.execute(f"SELECT tasks FROM users WHERE user_id = {user_id}")
    tasks = cursor.fetchall()
    return tasks


def db_delete(connection, user_id, task_id):
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM users WHERE user_id = {user_id} and task_id={task_id}")
    connection.commit()


def take_task_id(connection, user_id):
    cursor = connection.cursor()
    cursor.execute(f"SELECT user_id FROM users where user_id = {user_id}")
    if len(cursor.fetchall()) > 0:
        cursor.execute(f"SELECT max(task_id) from users where user_id = {user_id}")
        return cursor.fetchone()[0] + 1
    else:
        return 1


def db_new_task(connection, user_id, tasks):
    task_id = take_task_id(connection, user_id)
    cursor = connection.cursor()
    cursor.execute(f'insert into users (user_id, task_id, tasks) values (?, ?, ?)', [user_id, task_id, tasks])
    connection.commit()

