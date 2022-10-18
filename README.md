# Реализация HRU
## Установка виртуального окружения
* ### Клон репозитория
    > git clone https://github.com/shigetor/HRU.git

    > cd HRU

    * ### Создать виртуальное окружение
    > pip install virtualenv

    > python3 -m venv env

    > source env/bin/activate

* ## Список команд и их описание
    ### init() - инициализация системы
    ### create_user - создание пользователя
    ### create_object - создание объекта
    ### read_object - чтение объекта при наличии прав
    ### write_in_object -запись в объект
    ### delete_subject - удаление пользователя
    ### delete_object - удаление объекта
    ### give_access_to_user - передача прав другому пользователю владельцем\
