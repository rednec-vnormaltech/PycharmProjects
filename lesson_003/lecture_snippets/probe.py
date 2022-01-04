# Параметры передаются как ссылка

def elephant_to_free(some_list):
    elephant_found = 'elephant' in some_list
    if elephant_found:
        some_list.remove('elephant')
        print('Слон на свободе!!!')
    return elephant_found


zoo = ['lion', 'elephant', 'monkey', 'skunk', 'horse', 'elephant']

elephant_to_free(zoo)
print(zoo)

elephant_to_free(zoo)
print(zoo)

elephant_to_free(zoo)
print(zoo)

print(zoo)