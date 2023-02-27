import asyncio
import json

async def handle_client(reader, writer):

    # Очікуємо, поки клієнт надішле два числа
    data = await reader.read(1024)
    nums = json.loads(data.decode())

    # Виконуємо арифметичні операції
    add = nums[0] + nums[1]
    sub = nums[0] - nums[1]
    mul = nums[0] * nums[1]

    # Формуємо відповідь у форматі JSON
    response = {"Додавання": add, "Віднімання": sub, "Множення": mul}
    response_json = json.dumps(response)
    # Відправляємо результат клієнту
    writer.write(response_json.encode())
    await writer.drain()


async def main():
    # Створюємо серверний сокет
    server = await asyncio.start_server(handle_client, '127.0.0.1', 50)

    # Виводимо інформацію про сервер
    addr = server.sockets[0].getsockname()
    print(f"Сервер запущено на {addr[0]}:{addr[1]}")

    # Запускаємо серверну прослуховування
    async with server:
        await server.serve_forever()

# Запускаємо програму
asyncio.run(main())