import random

def int_float_string():
    el_type = random.choice(['int','float','str'])
    if el_type == 'int':
        return random.randint(1, 10) 
    elif el_type == 'float':
        return round(random.uniform(1.0, 2.0), 1) 
    else:
        return random.choice(['one', 'two', 'three', 'four','five']) 

def generate_dict():
    keys = ['one', 'two', 'three', 'four', 'five']
    dict1 = {}
    
    for key in keys:
        el_type = random.choice(['int', 'float'])
        if el_type == 'int':
            dict1[key] = random.randint(1, 10)  
        else:
            dict1[key] = round(random.uniform(1.0, 2.0), 1)  
    
    return dict1



def task1():
    list1 = [random.randint(1,100) for i in range(1,10)]
    print (list1,"\n",list1[::-1] )   

def task2():
    list1 = [random.randint(1,100) for i in range(1,10)]
    list2 = [random.randint(1,100) for i in range(1,10)]
    list3 =[]
    for i in range(0,len(list1)):
        if (i%2==0):
            list3.append(list1[i])
        else:
            list3.append(list2[i])
    print (list1,"\n",list2,"\n",list3 )

def task3():
    list1 = [int_float_string() for _ in range(10)]
    print (list1)
    list2 = list(set(list1))
    print(list2)

def task4():
    dict1 = generate_dict()
    print (dict1) 
    keys_value = {}
    for key, value in dict1.items():
        if value not in keys_value:
            keys_value[value] = [key]
        else:
            keys_value[value].append(key)

    list1 = [(value, keys) for value, keys in keys_value.items()]
    print(list1)

def task5():
    dict1 = generate_dict()
    dict2 = generate_dict()

    print(dict1)
    print(dict2)

    dict_values = set(dict1.values()).intersection(set(dict2.values()))
    dict3 = {key: value for key, value in dict1.items() if value in dict_values}

    print(dict3)



if __name__ == "__main__":
    
    task1()  
    task2()  
    task3()
    task4()
    task5()






