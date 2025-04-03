# Лабораторная работа 6

**Задание:**
Напишите корневой адрес работающего по https веб-приложения (+ ссылку на борд/репозиторий с кодом решения), которое по маршруту /size2json получает по имени поля image в формате multipart/form-data изображение в формате PNG и выдаёт JSON-строку вида {"width":123,"height":456}, содержащую, соответственно, ширину и высоту изображения в пикселях.

По маршруту /login приложение должно выдавать ваш логин в этой системе (MOODLE).

Требования: 

Все данные возвращаются в json, заголовки ответов должны быть соответствующие данным.
Формат ответа по маршруту /login {"author": "__ваш логин__"}
Если передана не картинка, возвращать json: {"result":"invalid filetype"}
Усложнения (дают: вероятность повышение итоговой оценки за модуль, прирост кармы и т.д.): 

Реализация дополнительных решений более чем с 1 фреймворком (Варианты: Node.js, Django, Go)
Реализация фронтэнда и отправка данных на сервер с использованием какого-либо фронтэнд-фреймворка.
Реализация асинхронной отправки данных, получение результата без перезагрузки страницы по отдельному маршруту, сохранение "состояния" (приложение помнит какой последний файл загружался и выводит данные по нему).
Вывод и отображение самого изображения на страницу с формой или другую страницу как thumbnail.


**Решение:**
Решение реализовано в Replit: 	[Борд](https://replit.com/@melnik3570/LR6?v=1)

Для проверки работы маршрута /size2json было сделано через Insomnia, которое вывело результат маршрута
