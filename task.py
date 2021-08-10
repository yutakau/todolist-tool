import json

class Task:
    def __init__(self, taskname, done):
        self.taskname = taskname
        self.done = done



def read_tasks():
    """　タスクを読み込む関数
    """

    with open('./tasks.json', encoding="utf-8") as f:
        tasks = json.load(f)
    return( tasks['tasks'] )


def write_tasks(tasklist):
    """　タスクを書き込む関数
    """
    tasks = {'tasks': tasklist}
    with open('./tasks.json', mode='w', encoding="utf-8") as f:
        json.dump(tasks,f)


def write_test():
    with open('./tasks.json', mode='w', encoding='utf-8') as f:
        json.dump({
            "tasks": [
                {"body": "牛乳を買う","done": True},
                {"body": "バナナを買う","done": True},
                {"body": "歯磨きする","done": False},
                {"body": "洗濯する","done": False},
                {"body": "皿を洗う","done": False}
            ]
        }, f)


def clear_tasks():
    pass



