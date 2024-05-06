import subprocess

def executar_comando(comando):
    try:
        # Executa o comando e captura a saída
        saida = subprocess.check_output(comando, shell=True, stderr=subprocess.STDOUT)
        # Decodifica a saída para string
        saida_str = saida.decode("utf-8")
        return saida_str
    except subprocess.CalledProcessError as e:
        # Se ocorrer um erro, imprime a mensagem de erro
        print("Erro ao executar o comando:", e.output)
        return None

# Exemplo de uso:
resultado = executar_comando("ls -l")
print(resultado)
