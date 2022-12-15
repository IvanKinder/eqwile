# eqwile
  pip install -r requirements.txt
  python manage.py runserver
  
  для простой авторизации в headers добавить credentials:
  
  admin:
  
  {
    "username": "admin",
    "password": "admin"
  }
  
  обычный юзер: 
  
  {
    "username": "test",
    "password": "12345678QWERTY"
  }
  
  существующие категории:
    id = 1
    id = 2
    id = 3
    
  существующие статусы:
    status_id = 1
    status_id = 2
    
  изменение статуса: api/status/
    прописывать в body put запроса, например:
      в виде объекта:
        {
            "tizer_id": "1",
            "status_id": "1"
        }
      в виде списка объектов:
        [
            {
                "tizer_id": "1",
                "status_id": "1"
            },
            {
                "tizer_id": "2",
                "status_id": "1"
            }
        ]
