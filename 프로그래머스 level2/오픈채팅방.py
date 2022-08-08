def solution(record):
    answer = []
    id_dict = dict()  
    commands = [list(r.split()) for r in record]  
    for command in commands:
        if command[0] == 'Enter' or command[0] == 'Change':  
            id_dict[command[1]] = command[2]

    for command in commands:
        if command[0] == 'Enter':
            answer.append(id_dict[command[1]] + "님이 들어왔습니다.")
        elif command[0] == 'Leave':
            answer.append(id_dict[command[1]] + "님이 나갔습니다.")
    return answer