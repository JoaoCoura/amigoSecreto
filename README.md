# Projeto Amigo Secreto 🎉

Este projeto é um sorteador de amigo secreto, desenvolvido em Python. Ele permite realizar sorteios de forma simples e eficiente, garantindo que nenhuma pessoa se tire e que não haja sorteios recíprocos (onde duas pessoas se tiram mutuamente).

## Funcionalidades

- **Sorteio Justo**: O sorteador impede que uma pessoa se auto-sorteie.
- **Verificação de Reciprocidade**: O código verifica que duas pessoas não se sorteiem mutuamente, evitando pares recíprocos.
- **Simplicidade**: Com poucos comandos, você fornece os nomes dos participantes e o sorteio é feito automaticamente.

## Como Usar 📋

1. Ao iniciar o programa, insira o número de amigos participantes.
2. Em seguida, forneça o nome de cada amigo, um de cada vez.
3. O sorteio será realizado automaticamente, e o programa exibirá a pessoa para quem cada amigo deverá dar um presente.

## Requisitos

- **Python 3.x** (desenvolvido e testado na versão mais recente).

### Exemplo de Uso

```plaintext
Número de amigos: 4
Amigo 1: João
Amigo 2: Maria
Amigo 3: Pedro
Amigo 4: Ana
```

Após fornecer todos os nomes, o programa exibirá os resultados do sorteio.

```plaintext
João tirou Ana
Maria tirou Pedro
Pedro tirou João
Ana tirou Maria
```

## Autor

- [João Pedro Basso Coura](https://www.linkedin.com/in/jpbcoura/)
