import sys
import requests
auth_params = {    
    'key': "0bdb5b6620d215e7947e8b575c3cb074",    
    'token': "692c9ee602c589403822649403d69493a245ae73e6149099c353ab38df7e4c1d", }
base_url = "https://api.trello.com/1/{}"
board_id = "mf03wDlz"            
def create_column(column_name):
	requests.post(base_url.format('boards') + '/' + board_id + '/lists', data={'name': column_name, **auth_params})

def read():
	lst = []
	
	
	# Получим данные всех колонок на доске:
	column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()      
      
    # Теперь выведем название каждой колонки и всех заданий, которые к ней относятся:      
	for column in column_data:
		# print(column['name'])    
        # Получим данные всех задач в колонке и перечислим все названия      
		
		task_data = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards', params=auth_params).json()      
		if not task_data:      
			print(column['name']+' Количество задач - 0')
			# print('\t' + 'Нет задач!')      
			continue
		# print(column['name'])	      
		for task in task_data:
			lst.append(task['name'])
		print(column['name']+' Количество задач - ', len(lst))
		for i in lst:
			print('\t' + i)
		# print(column['name'])
             
def create(name, column_name):      
    # Получим данные всех колонок на доске      
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()      
      
    # Переберём данные обо всех колонках, пока не найдём ту колонку, которая нам нужна      
    for column in column_data:

        if column['name'] == column_name:      
            # Создадим задачу с именем _name_ в найденной колонке      
            requests.post(base_url.format('cards'), data={'name': name, 'idList': column['id'], **auth_params})      
        break              
def move(name, column_name):    
    # Получим данные всех колонок на доске    
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()    
        
    # Среди всех колонок нужно найти задачу по имени и получить её id    
    task_id = None
    dct_task={}
    i=0    
    for column in column_data:    
        column_tasks = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards', params=auth_params).json()    
        # собираем все одинаковые задачи в словарь
        for task in column_tasks:    
            if task['name'] == name:    
                i+=1
                # task_id = task['id']
                print(i,task['id'],task['name'],column['name'])
                dct_task[i] = task
    # выбираем номер задачи, с которой хотим работать            
    n = input("Введите номер задачи, которую хотите переместить:")
    # находим id задачи для дальнейшй работы с ней
    task_id = dct_task[int(n)]['id']  
       
    # Теперь, когда у нас есть id задачи, которую мы хотим переместить    
    # Переберём данные обо всех колонках, пока не найдём ту, в которую мы будем перемещать задачу    
    for column in column_data:    
        if column['name'] == column_name:    
            # И выполним запрос к API для перемещения задачи в нужную колонку    
            requests.put(base_url.format('cards') + '/' + task_id + '/idList', data={'value': column['id'], **auth_params})    
            break  
if __name__ == "__main__":    
    if len(sys.argv) <= 1:    
        read()
    elif sys.argv[1] == 'create_column':    
        create_column(sys.argv[2])
    elif sys.argv[1] == 'create':    
        create(sys.argv[2], sys.argv[3])    
    elif sys.argv[1] == 'move':    
        move(sys.argv[2], sys.argv[3])  