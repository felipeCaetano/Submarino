# Submarino
Um submarino usando TDD - a partir do desafio do Buscapé

+ L e R para girar o submarino para esquerda ou direita,
+ M para mover o submarino e
+ U e D para subir ou descer o submarino.

Você deve desenvolver um sistema que processe uma série de comandos e faça a navegação desse submarino.

Para simplificar, leve em consideração que o submarino sempre começará no ponto (0, 0, 0, NORTE) e

que todo movimento quando o submarino estiver apontando para o NORTE, somará 1 ao eixo Y,

todo movimento quando o submarino estiver apontando para o LESTE somará 1 ao eixo X e

todo movimento para baixo diminuirá 1 do eixo Z.

Ah, vale lembrar que 0 no eixo Z é a superfície do oceano


## Entrada:

Os cientistas mandarão os comandos agrupados em uma única linha, como no exemplo:

```
LMRDDMMUU
```


## Saída:

A saída deverá conter a coordenada final do submarino junto com sua direção, como no exemplo:

```
-1 2 0 NORTE
```

## Exemplo de execução:


Dado a seguinte entrada:

```
RMMLMMMDDLL
```

A saída esperada é:

```
2 3 -2 SUL
```

Lembrando que a posição inicial do submarino é 0, 0, 0, NORTE

mais em: https://github.com/buscape-company/exercicios/tree/master/java
