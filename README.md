# summarization-marketing

WEB-application на streamlit для выделения из новостей ключевой информации.

Под капотом bert ([ссылка на источник](https://huggingface.co/IlyaGusev/mbart_ru_sum_gazeta)), обученный на новостях gazeta.ru, то есть его применение ограничено новостными сводками.

Для запуска приложения:
```
streamlit run main.py
```

Также есть возможноть запустить docker-compose, для этого билдим докер:
```
docker build -t summ .
```

После чего поднимаем compose:
```
docker-compose up -d
```
