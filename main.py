from config import RedisConfig as redis


redis = redis("data.txt")

# После получения лучше закоментировать set
# redis.set("Имя", "Вова")
# redis.set("Возраст", "73")
# redis.set("Страна проживания", "Мозамбик")
# redis.set("Город проживания", "Мухосранск")


# тут можно получить уже существующие значения. Если значений нет то сработает TypeError
try:
    value = redis.get("Имя")
    value2 = redis.get("Возраст")
    value3 = redis.get("Страна проживания")
    value4 = redis.get("Город проживания")
    print(value[0], value2[0], value3[0], value4[0], sep='\n')
    
    # А это просто удаляет данные
    # redis.delete('Имя')
except TypeError as e:
    print('я не нашел ключа с таким названием')

