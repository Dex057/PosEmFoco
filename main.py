import os
from dotenv import load_dotenv
from core import WebScraper, ServicoNotificacao, Usuario, Interesse

load_dotenv()

def main():
    print("=== INICIANDO SISTEMA DE MONITORAMENTO DE EDITAIS (MVP) ===")

    email_teste = "dex057ali03@gmail.com" 
    
    usuario_mvp = Usuario(
        nome="Pesquisador UFPA",
        email=email_teste,
        interesses=[
            Interesse(palavra_chave="Mestrado"),
            Interesse(palavra_chave="Doutorado"),
            Interesse(palavra_chave="Tecnologia"),
            Interesse(palavra_chave="Seleção"),
            Interesse(palavra_chave="Ciências"),
        ]
    )

    print(f"-> Usuário carregado: {usuario_mvp.nome}")
    print(f"-> Interesses ativos: {[i.palavra_chave for i in usuario_mvp.interesses]}")
    print("-" * 50)

    scraper = WebScraper()
    
    editais_encontrados = scraper.coletar_editais(usuario_mvp)

    print("-" * 50)
    print(f"Resumo da Busca: {len(editais_encontrados)} editais relevantes encontrados.")

    if editais_encontrados:
        try:
            notificador = ServicoNotificacao()
            notificador.notificar_usuario(usuario_mvp, editais_encontrados)
        except Exception as e:
            print(f"Erro ao tentar notificar: {e}")
            print("Verifique se o arquivo .env está configurado corretamente.")
    else:
        print("Nenhum edital compatível encontrado hoje. Nenhuma notificação enviada.")

    print("\n=== FIM DO PROCESSO ===")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário.")