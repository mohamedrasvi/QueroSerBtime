"""Este problema foi utilizado em 148 Dojo(s).
Todo número inteiro positivo pode ser representado pelo produto de potências de números primos (os chamados fatores primos).
Por exemplo o número 6 pode ser representado pelo produto do números primos 2 x 3.

Outros exemplos:

5 = 5 (números primos só tem um fator primo - ele mesmo)
100 = 2 x 2 x 5 x 5
198 = 2 x 3 x 3 x 11
276 = 2 x 2 x 3 x 23
Desenvolva um programa que dado um número inteiro positivo, retorne os seus fatores primos."""

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac
	
print primes(198)
