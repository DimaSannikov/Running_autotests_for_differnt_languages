# Задание: запуск автотестов для разных языков интерфейса

### Английский, Chrome
pytest test_items.py
pytest --language=en test_items.py
pytest --language=en --browser_name=chrome test_items.py
### Испанский, Chrome
pytest --language=es test_items.py
### Французский, Chrome
pytest --language=fr test_items.py
### Английский, Firefox
pytest --language=es --browser_name=firefox test_items.py
### Английский, Firefox
pytest --browser_name=firefox test_items.py
pytest --language=en --browser_name=firefox test_items.py
### Испанский, Firefox
pytest --language=es --browser_name=firefox test_items.py
### Французский, Firefox
pytest --language=fr --browser_name=firefox test_items.py