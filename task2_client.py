import asyncio
import json

async def send_numbers(server, host, nums):
    # Відкриваємо з'єднання з сервером
    reader, writer = await asyncio.open_connection(server, host)

    # Відправляємо запит на сервер
    request_json = json.dumps(nums)
    writer.write(request_json.encode())
    await writer.drain()

    # Очікуємо відповідь від сервера
    response = await reader.read(1024)
    response_json = json.loads(response.decode())

    # Повертаємо результат
    return response_json

# Запитуємо користувача про числа
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
nums = [a, b]

# Відправляємо запит на сервер та отримуємо результат
result = asyncio.run(send_numbers('127.0.0.1', 50, nums))

# Виводимо результат
print(f"Результат: {result}")