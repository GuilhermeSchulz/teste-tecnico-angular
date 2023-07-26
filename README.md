# Teste de conhecimentos python

## Objetivo
- Fazer o teste de python para a vaga de backend na Angular é absolutamente essencial. Se você estiver empolgado por esta oportunidade, saiba que isso não apenas demonstrará proficiência na linguagem, mas também mostra a capacidade de resolver problemas de forma autônoma e entender cenários de negócio.

## Objetivo do teste
- Criar um projeto para fazer cotações de frete:
1. Criar um projeto django com um app de cotação de fretes (Delivery);
1. Criar um modelo de pedidos (Order) com os campos: number, amount, weight, width, height, length, zip_from, zip_to;
1. Criar uma tela no admin para criar, e editar os pedidos;
1. Criar um modelo de cotações de fretes (Freight) com os campos: order (FK), carrier, delivery_time, delivery_cost, external_freight_id;
1. Criar uma action no modelo de Order para fazer o cálculo do frete via API (ver instruções abaixo) e gravar os resultados no modelo de Freight;
1. Colocar as entradas de Freight como inline no django admin do Order;

## Sobre API a consumir
- usar python requests para fazer chamada a API de cálculo de frete
- usar a documentação da plataforma MelhorEnvio (https://docs.menv.io/)
- usar o serviço de "Calculo de fretes (Pacote)" com seguro de R$ 100,00 e sem mão própria, com aviso de recebimento
- usar para autenticação Header Authorization tipo Bearer com chave: `eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImEzZWFiNTQ5MmU0M2Q1ZjIwZDY1NTk2MGNhNmU5NWQyMWQ5YjFiOGYwMDI2ZWJkMzA5OGI0NWViM2RmNGUwNzk4ZTU5NzMwMWMyMzJlMDdiIn0.eyJhdWQiOiI5NTYiLCJqdGkiOiJhM2VhYjU0OTJlNDNkNWYyMGQ2NTU5NjBjYTZlOTVkMjFkOWIxYjhmMDAyNmViZDMwOThiNDVlYjNkZjRlMDc5OGU1OTczMDFjMjMyZTA3YiIsImlhdCI6MTY4MDEwMjAwMCwibmJmIjoxNjgwMTAyMDAwLCJleHAiOjE3MTE3MjQ0MDAsInN1YiI6IjMxODg1OTMwLTYzZWUtNDAxOS04NWFiLTM4ZDRiODdkOTk2NyIsInNjb3BlcyI6WyJjYXJ0LXJlYWQiLCJjYXJ0LXdyaXRlIiwiY29tcGFuaWVzLXJlYWQiLCJjb21wYW5pZXMtd3JpdGUiLCJjb3Vwb25zLXJlYWQiLCJjb3Vwb25zLXdyaXRlIiwibm90aWZpY2F0aW9ucy1yZWFkIiwib3JkZXJzLXJlYWQiLCJwcm9kdWN0cy1yZWFkIiwicHJvZHVjdHMtZGVzdHJveSIsInByb2R1Y3RzLXdyaXRlIiwicHVyY2hhc2VzLXJlYWQiLCJzaGlwcGluZy1jYWxjdWxhdGUiLCJzaGlwcGluZy1jYW5jZWwiLCJzaGlwcGluZy1jaGVja291dCIsInNoaXBwaW5nLWNvbXBhbmllcyIsInNoaXBwaW5nLWdlbmVyYXRlIiwic2hpcHBpbmctcHJldmlldyIsInNoaXBwaW5nLXByaW50Iiwic2hpcHBpbmctc2hhcmUiLCJzaGlwcGluZy10cmFja2luZyIsImVjb21tZXJjZS1zaGlwcGluZyIsInRyYW5zYWN0aW9ucy1yZWFkIiwidXNlcnMtcmVhZCIsInVzZXJzLXdyaXRlIiwid2ViaG9va3MtcmVhZCIsIndlYmhvb2tzLXdyaXRlIl19.PTb06vQtUANuSa246Atljh7_OUbs7y0nmd1ARStq7PCgKSQCQ6MSaZSsRoSJ6P60EXOqSMndmiRVXfjz8c8sXW0L-cLjmuRM8mvG1DZ9VtfgLUmNd7pc-5kVpJh91ICVoQE7AQjXJkQkS3NdyJYr4HoMLlfNmuwJZGQUOpM2SS-SotXHP2zDMU43J61gjd3D-0Mcv_rVKpq46FAK5ZPfZlEE5e8ednepRY7EtVrM9XmVnVl771yUnKtE7DVvtCCpFIc2YfkCTNHLyGasG9wPCfoyXPZd5zBqsEIKJz2sbyoXrAIRdSUScoH-eD4ulLFH_z93-ej2Py8X6LogPfaIqE7RzEFyl4ZLNvdABjn7dQ1edcWbA8xQu8lMIFSdkwSBbcJ_JsNVFWlnh25DTcLItzaKF9mRSZuBmKQCz5xVuomGFQmX3ucw2uyTyoC3PItRhDQbDDhaY11IECyMbvy--nr3HhTzf2n3JpUsCFMk8vZwifvS0G6Xip_AtHqBDYiIrJXJOo4phybBLzuKw3E4SCm78AJsJAAWOkw4Y_nACF0K4l3hdrchpLPOsGA3Twi3oVIo6CM41SCC0orvfShGeRUOX1jCYxa63rkiQC1qlg-FnI3_aHrML01XI4wTHf-QS_MEXWNl8rQtmEYUkZBqcS5LTV0-wb3FHi691FwlD9A`

## Mais informações sobre o teste
- se precisar de mais campos nos modelos, pode incluir;
- se precisar de mais informações sobre funcionamento da API, a documentação é aberta e o link está acima;
- os nomes dos campos estão em inglês e são auto explicativos, mas para facilitar:
  - order.number - todo pedido tem um número, este não é o id mas é um identificador único do pedido;
  - carrier - é o nome da empresa e serviço da entrega (ex: Correios - Sedex)
  - zip_from/zip_to - é o código do cep de origem e destino

## Diferenciais
- Criar um teste unitário
- Ter admin configurado
- Usar linux
  
## Itens que serão avaliados e modo de entrega
- tempo levado para entregar;
- qualidade das dúvidas (se houver);
- beleza e organização de códigos e telas;
- após terminar, mandar o link do repositório, porém é mais importante um video do app rodando passando por todos os passos (pode ser em localhost)
- se o video for gravado em linux, será um extra!
