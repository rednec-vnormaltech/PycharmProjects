import socket
#Простой сканер портов

# IP-адрес, который нужно отсканировать
ip = '127.0.0.1'
ip1 ='213.183.117.56'#внешний платный ip
ip2 = '192.168.31.45'# внутренний локальная сеть (в свойствах написано 192.168.31.45/24)
count=0
# Просканировать все порты от 1 до 65535
for port in range(1, 65536):
    # Создаем сокет и устанавливаем его на неблокирующий режим
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.001)

    # Пытаемся установить соединение с целевой машиной через текущий порт
    try:
        result = s.connect_ex((ip1, port))
        if result == 0:
            print(f'Port {port} is open')
            count=count+1
            print(count)

    except:
        print(f'Connection to {ip1} on port {port} failed')

    # Закрываем соединение с сокетом
    s.close()