# Chat entre Clientes, manejado pelo Servidor 🔔

## Descrição do Projeto
Nesse projeto tentamos criar uma maneira simples de comunicação entre clientes em que suas mensagens são intermediadas pelo servidor, onde serão salvos as entradas de clientes, a quantidade de clientes ativas, as portas de entrada e os IPs dos clientes.
O cliente ao acessar o servidor deve escolher um nome por qual estará enviando suas mensagens.
As mensagens enviadas e os nomes escolhidos pelo cliente são codificadas pelo "utf-8", para facilitar o entedimento das mensagens.
As mensagens rodarão por um loop infinito onde o cliente pode mandar mensagem quando e da forma que quiser.
Elas rodarão por um for como uma espécie de broadcast e pela função threading aparecerão para todos os usuários conectados.
A quantidade de usuários conectados será mostrada, assim como o IP do computador conectado e uma mensagem aparecerá no servidor conforme os clientes vão se conectando, listen() coloca o servidor em modo de escuta esperando a conexão dos clientes.

## Possíveis melhorias
Gostariamos de ter adicionado um log onde seria relatado o historico de conversa, e uma criptografia para a proteção de tais dados
Assim como uma maneira do servidor se comunicar diretamente com um cliente

## Para rodar a aplicação
apenas abrir e executar o código "server-project.py" e abrir e executar o código "cliente-project.py", digitar o nome a aparecer no chat e trocar mensagens com outros usuários, o código cliente pode ser aberto várias vezes para testar a comunicação multi-thread e como o nosso projeto se comporta com vários clientes ao mesmo tempo, uma das especificações do projeto.
