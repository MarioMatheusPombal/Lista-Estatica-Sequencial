import Les

listaA= Les.Les()
listaB= Les.Les()
listaA.InserirInicio('B')
listaA.InserirInicio('A')
listaA.InserirFim('C')
listaA.show()
listaA.InserirAposDet('Z','C')
listaA.show()
'''
listaB.InserirInicio(listaA.getPrim())
listaB.InserirFim(listaA.getUlt())
#listaB.InserirFim(listaB.getUlt())
listaB.InserirInicio('A')
listaA.show()
listaB.show()
listaA.InserirAposDet('X','A')
listaB.InserirAposDet('X','B')
listaA.show()
listaB.show()
listaA.RemoverInicio()
listaB.RemoverInicio()
if listaA.getUlt()==listaB.getUlt():
    print('As Listas tem os últimos valores iguais')
if listaA.getPrim()==listaB.getPrim():
    print('As listas tem seus primeiros valores iguais')
if listaA.getQuant()==listaB.getQuant():
    print('As listas tem a mesma quantidade de elementos')
for i in range(listaA.getQuant()):
    listaA.RemoverInicio()
for i in range(listaB.getQuant()):
    listaB.RemoverFim()''' 




