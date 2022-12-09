****************  ДОКУМЕНТАЦИЯ К API  ****************

*ПРОЕКТ НАПИСАН НА Django Rest Framework
*РАЗВЕРНУТ на хостинге BEGET(http://artkong1.beget.tech/admin)


РЕАЛИЗОВАНО:

*СОЗДАНИЕ НОВОГО АККАУНТА
*ДОБАВЛЕНИЕ И ПОЛУЧЕНИЕ ИНФОРМАЦИИ О ПАЦИЕНТАХ/ВРАЧАХ
*ПРИВЯЗКА ПАЦИЕНТА К ВРАЧУ
*СОЗДАНИЕ, РЕДАКТИРОВАНИЕ НОВОГО ПОСТА(ДЛЯ ВРАЧЕЙ)
*ПОЛУЧЕНИ ВСЕХ ПОСТОВ/ПОЛУЧЕНИ ПОСТОВ ПО КОНКРЕТНОМУ ТЭГУ





РЕГИСТРАЦИЯ
method: POST
url: http://artkong1.beget.tech/api/v1/auth/users/


АВТОРИЗАЦИЯ
method: POST
url: http://artkong1.beget.tech/api/v1/token/
response: { "refresh": <refresh-token>, "acсess": <access-token> }


ОБНОВИТЬ ACCESS TOKEN
method: POST
url: http://artkong1.beget.tech/api/v1/token/refresh
response: { "refresh": <refresh-token>, "acсess": <access-token> }


ДОБАВЛЕНИ ДОПОЛНИТЕЛЬНОЙ ИНФОРМАЦИИ О ПАЦИЕНТЕ
method: POST
url: http://artkong1.beget.tech/api/v1/patient/


ПОЛУЧЕНИ ИНФОРМАЦИИ О ВСЕХ ПАЦИЕНТАХ
method: GET
url: http://artkong1.beget.tech/api/v1/patient/


ПОЛУЧЕНИ ИНФОРМАЦИИ О ПАЦИЕНТЕ ПО ID
method: GET
url: http://artkong1.beget.tech/api/v1/patient/<ID>/


ДОБАВЛЕНИ ДОПОЛНИТЕЛЬНОЙ ИНФОРМАЦИИ О ВРАЧЕ
method: POST
url: http://artkong1.beget.tech/api/v1/doctor/


ПОЛУЧЕНИ ИНФОРМАЦИИ О ВСЕХ ВРАЧАХ
method: GET
url: http://artkong1.beget.tech/api/v1/doctor/


ПОЛУЧЕНИЕ ИНФОРМАЦИИ О ВРАЧЕ ПО ID
method: GET
url: http://artkong1.beget.tech/api/v1/doctor/<ID>/


ПРИКРЕПЕЛНИ ПАЦИЕНТА К ВРАЧУ
method: POST
url: http://artkong1.beget.tech/api/v1/patient-doctor/


ДОБАВЛЕНИЕ НОВОГО ПОСТА
method: POST
headers:  "Authorization": "Token <access-token>
url: http://artkong1.beget.tech/api/v1/quiz/


ПОЛУЧЕНИE ВСЕХ ПОСТОВ
method: GET
url: http://artkong1.beget.tech/api/v1/quiz/


ПОЛУЧЕНИE ПОСТОВ ПО ТЕГУ
method: GET
url: http://artkong1.beget.tech/api/v1/quiz-tag/<quiz-tag>/





