#include "./wiringPi/wiring.h"
#include "../Telegram/tg.h"

void SendMessage(int chat_id, char[] msg)
{
    int port = 443;
    char host[] = "api.telegram.org"; // Адрес и порт всегда одинаковые
    // Создадим шаблон HTTP запроса для отправки сообщения, в виде форматированной строки
    char header[] = "POST /bot352115436:AAEAIEPeKdR2-SS7p9jGeksQljkNa9_Smo0/sendMessage HTTP/1.1\r\nHost: files.ctrl.uz\r\nContent-Type: application/json\r\nContent-Length: %d\r\nConnection: close\r\n\r\n%s";
    // Шаблон тела для отправки сообщения
    char tpl[] = "{\"chat_id\":%d,\"text\":\"%s\"}";
    char body[strlen(tpl) + strlen(msg) + 16];
    bzero(body, strlen(tpl) + strlen(msg) + 16);
    sprintf(body, tpl, chat_id, msg); // Как printf, только печатаем в char[]
    char request[strlen(header) + strlen(body) + 4];
    bzero(request, strlen(header) + strlen(body) + 4);
    sprintf(request, header, strlen(body), body);
    // Подготовили наш запрос, теперь создаем подключение
    struct hostent *server;
    struct sockaddr_in serv_addr;
    int sd;
    sd = socket(AF_INET, SOCK_STREAM, 0);
    if (sd < 0)
        exit(-5);
    server = gethostbyname(host); // Данная функция получает ip и еще некоторые данные по url
    if (server == NULL)
        exit(-6);
    bzero(&serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(portno);
    memcpy(&serv_addr.sin_addr.s_addr, server->h_addr, server->h_length);
    if (connect(sd, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)
    {
        exit(-6);
    }
    SSL_CTX *sslctx = SSL_CTX_new(TLSv1_client_method());
    SSL *cSSL = SSL_new(sslctx);
    SSL_set_fd(cSSL, sfd);
    SSL_connect(cSSL);
    SSL_write(cSSL, request, (int)strlen(request)); // Отправляем наш запрос, в идеале его надо отправлять так же как мы считывали данные, то есть с проверкой на кол-во отправленных байт
    char str[1024];
    SSL_read(cSSL, str, 1024); // Считываем ответ и закрываем соединение
    SSL_clear(cSSL);
    SSL_CTX_free(sslctx);
    close(sd);
}

int main()
{

    SSL_CTX *sslctx = InitializeSSL("cert.pem"); // Созданный нами файл из приватного ключа и публичного сертификата
    int sd = InitializeSocket(8443);             // Порт который вы указали при установке WebHook
    listen(sd, 5);
    // Слушаем подключения на созданном сокете
    wiringPiSetupGpio();
    pinMode(SYGNAL, INPUT);
    // pullUpDnControl(SYGNAL, PUD_DOWN);
    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);
    pinMode(LED3, OUTPUT);
    pinMode(RELE, OUTPUT);

    // digitalRead();
    while (1)
    {
        int client = accept(sd, NULL, NULL); // функция accept ждет новое подключение, в качестве параметров принимает сокет, указатель на структуру sockaddr, и указатель на размер этой структуры и записывает туда данные подключения, так как нам необязательно знать подробности подключения отправим NULL, функция возвращает сетевой дескриптор.
        SSL *ssl = SSL_new(sslctx);          // Cоздаем ssl дескриптор
        SSL_set_fd(ssl, client);             // Переключаем обычный дескриптор на защищенный
        if (SSL_accept(ssl) <= 0)
        { // Пытаемся принять подключение, если ошибка то закрываем соединение и возвращаемся к началу цикла
            SSL_clear(ssl);
            close(newsd);
        }
        else
        {

            // Для увеличения производительности будем использовать fork() и обрабатывать соединение в дочернем процессе, а родительский процесс вернем к ожиданию новых подключений
            int pid = fork();
            if (pid != 0)
            { // Если это родитель, то закрываем подключение и возвращаемся к началу цикла
                SSL_clear(ssl);
                close(newsd);
            }
            else
            {
                char[] response = "HTTP/1.1 200 OK\r\nConnection: close\r\n\r\n"; // Наш HTTP response
                char header[1024];
                bzero(header, 1024); // Выделили массив для записи в него заголовков запроса и на всякий случай занулили там все записи.
                int s = 0;
                int n = 0;
                while (strcmp(header + s - strlen("\r\n\r\n"), "\r\n\r\n") != 0)
                {                                     // strcmp Сравнивает две строки и если они равны возвращает 0, в нашем случае сравниваем последние strlen("\r\n\r\n") байт с "\r\n\r\n", то есть ищем конец заголовка
                    n = SSL_read(ssl, header + s, 1); // Считываем данные по одному байту в header + s, s - общее кол-во считанных байт
                    s += n;                           // n - кол-во считанных байт за раз
                }
                // Все, заголовки считаны, теперь нам надо проверить метод, uri, content-type и вытащить content-length запроса.
                if (strstr(header, "POST /(URI указанный при установке WebHook) HTTP/1.1\r\n") == NULL)
                { // Ищем вхождение строки POST .... в header, если его нет то возвращается NULL, значит пришел неверный запрос, закрываем подключение и завершаем дочерний процесс
                    SSL_clear(ssl);
                    close(client);
                    exit(0);
                }
                // Также проверим тип данных, должен быть application/json;
                if (strstr(header, "Content-Type: application/json") == NULL)
                {
                    SSL_clear(ssl);
                    close(client);
                    exit(0);
                }
                // Если все нормально, то узнаем размер тела
                int len = atoi(strstr(header, "Content-Length: ") + strlen("Content-Length: ")); // strstr возвращает указатель не первое вхождение указанной строки, то есть на "Content-Length: ", а кол-во байт записано дальше после этой строки, поэтому прибавляем длину строки "Content-Length: " и приводим строку к типу int функцией atoi(char *);

                char body[len + 2];
                bzero(body, len + 2); // Создаем массив для тела, на этот раз мы точно знаем сколько байт нам понадобится, но создаем с запасом, дабы не оказалось что в памяти сразу после нашей строки что-то записано
                n = 0;
                s = 0;
                while (len - s > 0)
                {                                         // Так как мы четко знаем сколько данных нам надо считать просто считываем пока не считаем нужное кол-во
                    n = SSL_read(ssl, body + s, len - s); // Конечно можно было считать целиком все данные, но бывают случаи при плохом соединении, за раз все данные не считываеются, и функция SSL_read возвращает кол-во считанных байт
                    s += n;
                }

                char msg[50];

                if (body == "mode1")
                {
                    state = MODE1;
                    msg = "Switch to mode1.";
                }
                else if (body == "mode2")
                {
                    state = MODE2;
                    msg = "Switch to mode2.";
                }
                else if (body == "mode3")
                {
                    state = MODE3;
                    msg = "Switch to mode3.";
                }
                else
                {
                    msg = "Bad request.";
                }

                // На этом получение данных окончено, отправим наш http response и закроем соединение SSL_write(ssl, response, (int)strlen(response));
                SSL_clear(ssl);
                SSL_free(ssl);
                close(client);
                // Так как у нас "Hello, World" бот то мы будем просто отвечать на любое сообщение "Hello, World!", но нам нужно знать кому отправлять сообщение для это из тела запросы надо вытащить параметр chat_id
                int chat_id = atoi(strstr("\"chat_id\":") + strlen("\"chat_id\":")); // То же самое что и с Content-Length
                // Осталось только отправить сообщение, для этого лучше создадим отдельную функцию SendMessage

                SendMessage(chat_id, msg); // Описание функции далее

                exit(0); // Завершаем дочерний процесс
            }
        }

        uint8_t sygnal_val = digitalRead(SYGNAL);

        switch (state)
        {
        case MODE1:
            void turnoff_mode2();
            void turnoff_mode3();
            void turnoff_releoff();
            digitalWrite(LED1, led1_state);
            if (sygnal_val)
            {
                rele_state = 1;
            }
            else
            {
                turnoff_mode1();
                set_releoff();
            }

            break;

        case MODE2:
            void turnoff_mode1();
            void turnoff_mode3();
            void turnoff_releoff();
            long current_time = millis();
            if (mode2_start_time < current_time - MODE2_INTERVAL)
            {
                turnoff_mode2();
                set_mode1();
            }

            break;
        case MODE3:
            void turnoff_mode1();
            void turnoff_mode2();
            void turnoff_releoff();
            unsigned long currentMillis = millis();
            if (currentMillis - previousMillis >= BLINK_INTERVAL)
            {
                led1_state = !led1_state;
                led3_state = !led3_state;
                digitalWrite(LED1, led1_state);
                digitalWrite(LED3, led3_state);
                previousMillis = currentMillis;
            }

            break;
        case RELEOFF:
            // send to tg bot one message

            break;
        }

        digitalWrite(RELE, rele_state);
    }
}