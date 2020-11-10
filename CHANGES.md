# Changelog

## 2020-11-10

### changes

* A função `download` recebeu o prefixo `async` e não utiliza mais o *Thread* para requisições, agora é feita com paralelismo, o que forçou uma mudança na classe `HTTPDownloader`. Para não apagar a função foi criada uma `AioHTTPDownloader(aiobject)`.