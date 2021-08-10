import argparse
from task import Task, write_test, read_tasks, write_tasks

def cmd_add(task):
    print("ADD",task)
    tasklist = read_tasks()
    
    tasklist.append({'body': task, 'done': False})
    print(tasklist)
    write_tasks(tasklist)
        

def cmd_done(targettask):
    tasklist = read_tasks()

    index = tasklist.index({'body':targettask, 'done': False})
    tasklist[index] = { 'body':targettask, 'done': True }
    print(tasklist)
    write_tasks(tasklist)
    

def cmd_list():
    tasklist = read_tasks()

    print("# Todo")
    for task in tasklist:
        if task['done'] == False:
            print("* ", task['body'])

    print()
    print("# Done")
    for task in tasklist:
        if task['done'] == True:
            print("* ", task['body'])





def cmd_clear():
    tasklist = read_tasks()
    update_tasklist = []

    for task in tasklist:
        if task['done'] == False:
            update_tasklist.append(task)
            
    write_tasks(update_tasklist)

def cmd_test():
    write_test()


def main():
    parser = argparse.ArgumentParser(description="タスク管理ツール")
    subparsers = parser.add_subparsers(dest='action')

    parser_add = subparsers.add_parser('add', help="タスクを追加する")
    parser_add.add_argument('task', action='store')
    
    parser_clear = subparsers.add_parser('clear', help="完了タスクを消去")

    parser_list = subparsers.add_parser('list', help="タスクの一覧表示")

    parser_wtest = subparsers.add_parser('wtest')

    parser_done = subparsers.add_parser('done', help="タスクを完了にする")
    parser_done.add_argument('task', action='store')

    args = parser.parse_args()
    if args.action == 'add':
        cmd_add(args.task)
    elif args.action == 'done':
        cmd_done(args.task)
    elif args.action == 'clear':
        cmd_clear()
    elif args.action == 'list':
        cmd_list()
    elif args.action == 'wtest':
        cmd_test()


if __name__ == "__main__":
    main()