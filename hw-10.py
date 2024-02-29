import requests


# requests.get(url=url)                                   # запрос, получить данные
# requests.post(url=url, data=data, headers=headers)      # запрос, отправить данные
# requests.put(url=url, data=data)                        # запрос, полное изменение данных
# requests.patch(url=url, data=data,)                     # запрос, частичное изменение данных
# requests.delete(url=url)                                # запрос, удаление данных


url = 'https://jsonplaceholder.typicode.com/posts'
response_get = requests.get(url)                          # запрос, получить данные


print('1_response: ________________________________')
print(response_get)
print('2_response.reason:__________________________')
print(response_get.reason)
print('3_response.headers:_________________________')
print(response_get.headers)
print('4_response.text:____________________________')
print(response_get.text)
print('5___________________________________________')


print('6___________________________________________')
# Сохраняем текст запроса (html_code) в файл
html_code = response_get.text
with open("page.html", "w", encoding="utf-8") as file:
    file.write(html_code)
print('6___________________________________________')


print('7___________________________________________')
# Читаем заголовки сайта
for header, value in response_get.headers.items():
    print(f'{header}: {value}')
print('7___________________________________________')
