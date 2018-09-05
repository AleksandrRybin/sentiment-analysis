# Анализ тональности текстов

- Классификатор обучен оценивать тональность __негативная__ *или* __положительная__ отзывов на мобильные телефоны на русском языке.

- Для взаимодействия используется _веб интерфейс_.

## Запуск

1) Находясь в папке проекта запустить файл _demo.py_ - __python demo.py__

2) В браузере передти по адресу _localhost:5000_

## Использование

1) Ввести в текстовое поле отзыв (убрать изначально находящийся там текст для примера)

2) Нажать кнопку __"Оценить"__

## Примеры работы

### Отзыв

    Достоинства: кнопки пластмассовые

    Недостатки: симку теряет через 1-2 минуты, разборчивость речи ниже всякой критики

    Комментарий: нокия упала по качеству очень сильно

![Результат](https://github.com/AleksandrRybin/SentimentAnalysis/raw/master/images/example1.png)

### Ещё примеры

В файла *example_reviews.txt* находятся разные примеры отзывов с разным количеством звёзд
Работу классификатора можно оценить на них

## Требуемые пакеты

- Flask

- Scikit-learn