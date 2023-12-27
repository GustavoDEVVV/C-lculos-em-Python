#Sucessor e antecessor

n = int(input('Digite um número:'))

a = n -1
s = n +1

print("O antecessor de {} é {} e o sucessor de {} é {}" .format(n,a,n,s))

#deixando o codigo mais limpo
print("O antecessor de {} é {} e o sucessor de {} é {}" .format(n,(n-1),n,(n+1)))
#Fazendo isso, você não precisa criar duas variáveis para funcionar, basta fazer como está acima.


#Dobro, triplo e raiz
num = int(input('Digite um número: '))

div = num ** (1/2)

print("O Dobro de {} vale {}." .format(num,(num*2)))
print("O Triplo de {} vale {}." .format(num,(num*3)))
print("A raiz quadrada de {} é igual a {:.2f}" .format(num,div))

#":.2f" é usado para formatar o número exibindo-o com duas casas decimais.
#Ao invés de fazer "div = num ** (1/2)", você pode usar "pow(num, 1/2)". Neste caso, `num` é o número do qual você deseja calcular a raiz quadrada, e `1/2` representa a potência da raiz.


#Calcular média

n1 = float(input("Digite a primeira nota: \n"))
n2 = float(input("Digite a segunda nota: "))

#Pode tanto usar o ".format" como fazer do jeito tradicional: `media = (n1 + n2) / 2`.

print("a media entre {:.1f} e {} vai ser {}" .format(n1,n2,(n1 + n2) /2))

#Conversor de medidas

#vamos utilizar as medidas em METROS.

#------tabela--------
#km hm dam m dm cm mm
#--------------------


medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A media de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida,cm,mm))



#tabuada

num = int(input('Digite um numero inteiro: '))

print('-' *12)
print('{} x {:2} = {}'.format(num,1, num*1))
print('{} x {:2} = {}'.format(num,2, num*2))
print('{} x {:2} = {}'.format(num,3, num*3))
print('{} x {:2} = {}'.format(num,4, num*4))
print('{} x {:2} = {}'.format(num,5, num*5))
print('{} x {:2} = {}'.format(num,6, num*6))
print('{} x {:2} = {}'.format(num,7, num*7))
print('{} x {:2} = {}'.format(num,8, num*8))
print('{} x {:2} = {}'.format(num,9, num*9))
print('{} x {:2} = {}'.format(num,10, num*10))
print('-' *12)

#Este símbolo "print('-' * 12)" serve para fazer as linhas acima e abaixo. Em Python, podemos utilizar esse modelo para multiplicar strings.


#Convertendo moedas

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 3.27
print('com {:.2f} você pode comprar US${:.2f}'.format(real,dolar))

#`{:.2f}` é usado para formatar o número exibindo-o com duas casas decimais, semelhante ao formato de dinheiro padrão. Agora, você pode usar sua imaginação para aplicar isso a outras moedas existentes.


#Pintando uma parede

#Digamos que você deseja pintar uma parede e não sabe quanto de tinta usar. Pois bem, vamos calcular a altura e largura e, logo após, determinar quanto de tinta será necessário.

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

área = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².' .format(largura,altura,área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}l de tinta' .format(tinta)) 

#calcular %

preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))



salário = float(input('Qual é o salário do Funcionário? R$'))
novo = salário + (salário * 15/100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))

#conversor de temperaturas

c = float(input('Informe a temperatura em C: '))
f = 9 * c / 5 + 32
print('A temperatura de {}C corresponde a {}F'.format(c,f))


#aluguém de carros

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}' .format(pago))

