
# Тестовое на позицию backend-разработчика от Avito Tech: 

создать сервис для хранения и подачи объявлений, объявления должны храниться в базе данных, а сам сервис должен предоставлять API, работающее поверх HTTP в формате JSON.

📝 Требования:
▫️язык: Python, любые фреймворки;
▫️код должен быть выложен на github;
▫️необходимо реализовать 3 метода: получение списка объявлений, получение одного объявления, создание объявления;
▫️реализовать валидацию полей (не больше 3 ссылок на фото, описание не больше 1000 символов, название не больше 200 символов).

Как должны работать сами методы❓

1️⃣ Метод получения списка объявлений:
▫️нужна пагинация, на одной странице должно присутствовать 10 объявлений;
▫️нужна возможность сортировки: по цене (возрастание/убывание) и по дате создания (возрастание/убывание)
▫️поля в ответе: название объявления, ссылка на главное фото (первое в списке), цена.

2️⃣ Метод получения конкретного объявления:
▫️обязательные поля в ответе: название объявления, цена, ссылка на главное фото;
▫️опциональные поля (можно запросить, передав параметр fields): описание, ссылки на все фото.

3️⃣ Метод создания объявления:
▫️принимает все вышеперечисленные поля: название, описание, несколько ссылок на фотографии (сами фото загружать никуда не требуется), цена;
▫️возвращает ID созданного объявления и код результата (ошибка или успех).

👾Усложнения
Не обязательно, но задание может быть выполнено с любым числом усложнений:
▫️написаны юнит тесты;
▫️контейнеризация – возможность поднять проект с помощью docker-compose up;
▫️кеширование – для увеличения скорости ответа от сервера, может быть добавлено кеширование (Redis/Memcached).

Архитектура сервиса:

![image](https://github.com/user-attachments/assets/4dec20fa-5bc8-4879-9bae-c40bcf505301)

