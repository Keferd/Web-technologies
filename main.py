#подключение flask из библиотеки lapapp
from labapp import app
#запуск приложения
if __name__=='__main__':
    app.run(host='0.0.0.0',port=8888)
    
