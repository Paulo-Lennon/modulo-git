"""
Desafio Módulo Git

Neste arquivo você encontrará funções **incompletas** que representam
tarefas relacionadas ao aprendizado de Git e GitHub.

Seu objetivo é:
- Criar uma issue para cada função.
- Implementar a função em uma branch específica.
- Fazer commit, criar tag e abrir Pull Request.
- Repetir o processo até concluir todas as funções.

Boa sorte e bons commits! 🚀
"""

def mostrar_mensagem_inicial():
    
    mensagem = "Bem-vindo ao Desafio de Git!"
    print(mensagem)
    return mensagem

def listar_comandos_git_basicos():
    """
    Retorna uma lista com os principais comandos básicos do Git.
    Exemplo de saída:
    ["git init", "git add", "git commit", "git status", "git push"]
    """
    pass


def criar_mensagem_commit(funcao_nome):
    
    mensagem = f"Implementa função {funcao_nome}"
    return mensagem


def verificar_tag_valida(tag):    
    if len(tag) == 4 and tag[0] == "v" and tag[2] == "." and tag[1].isdigit() and tag[3].isdigit():
        return True
    elif len(tag) == 5 and tag[0] == "v" and tag[2] == "." and tag[1].isdigit() and tag[3:].isdigit():
        return True
    else:
        return False


def gerar_relatorio_final(funcoes_concluidas):
    """
    Recebe uma lista com os nomes das funções implementadas
    e retorna uma mensagem final do desafio.

    Exemplo:
    gerar_relatorio_final(["mostrar_mensagem_inicial", "listar_comandos_git_basicos"])
    ->
    "Desafio concluído! 2 funções implementadas com sucesso."
    """
    pass
