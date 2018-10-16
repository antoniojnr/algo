# Funções

De forma simples e direta, funções são um trecho de código que pode ser chamado pelo nome. O uso de funções permite ao programador dividir e organizar o código em blocos que podem ser reutilizados.

O trecho de código a seguir mostra a definição de uma função que imprime `"Hello world!"` na saída padrão. Para definir uma função, usa-se a palavra-chave `def`, seguida do nome da função e, finalmente, seus parâmetros entre parênteses - veremos isso a seguir.

```python
def imprime():
  print "Ola, mundo!"
```

Para chamar uma função, usa-se seu nome seguido de parênteses `()`. Nada é passado dentro dos parênteses se a função não requer parâmetros. Por exemplo, a chamada da função `imprime()` executará o bloco que foi definido dentro dela: `print "Ola, mundo!"`, neste caso.

Os parâmetros da função são passados entre parênteses na sua definição. Esses parâmetros serão variáveis válidas apenas dentro do bloco da função. A seguir, a função `imprime()` foi modificada para receber um parâmetro `nome`.

```python
def imprime(nome):
  print "Ola, {}!".format(nome)
```

Uma função pode ter mais de um parâmetro. Neste caso, os parâmetros são separados por vírgula, como na declaração da função `soma()` a seguir.

```python
def soma(a, b):
  resultado = a + b
  print "O resultado é: {:d}".format(resultado)
```

Algumas funções retornam um resultado, que pode ser reutilizado em expressões no seu código. Abaixo, a função `soma()` foi reescrita para retornar o resultado, em vez de imprimi-lo na saída padrão. Para retornar um resultado de uma função, use a palavra-chave `return`.

```python
def soma(a, b):
  resultado = a + b
  return resultado
```

O retorno da função deve sempre ser a última linha do bloco. Exceto quando for utilizado dentro de condicionais ou laços de repetição, como no exemplo a seguir.

```python
def calcular(a, b, op):
  if op == 'soma':
    return a + b
  else if op == 'subtracao':
    return a - b
```

É preciso tomar cuidado com o retorno de funções cuja execução pode tomar múltiplos caminhos, como a função `calcular()` acima. Esta função pode retornar um resultado ou não, dependendo dos parâmetros passados. Por exemplo, caso o parâmetro `op` não seja um dos valores esperados nas condições, então a função retornará `None`, que representa um resultado nulo.

Você pode definir funções e escrever seu código em um único script Python. Mas, futuramente, você verá formas melhores de organizá-lo em módulos ou classes.

## Exercícios

Reimplemente as seguintes funções de Python:
1. `len()`
2. `range(a, b)` (implemente apenas o `range()` que leva dois parâmetros)
3. `in(a, b)` (esta função verifica se o elemento ou caractere `a` existe na lista ou string `b`)
