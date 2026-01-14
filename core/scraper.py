from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from .modelos import Edital # pode utilizar o init também

class WebScraper:
    def __init__(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.url_fonte = "https://ufpa.br/?post_type=editais" 

    def coletar_editais(self, usuario):
        print("Iniciando scraping no site da UFPA...")
        self.driver.get(self.url_fonte)
        
        editais_relevantes = []
        palavras_chave = [i.palavra_chave.lower() for i in usuario.interesses]
        
        pagina_atual = 1
        max_paginas = 3 

        try:
            while pagina_atual <= max_paginas:
                print(f"--- Lendo página {pagina_atual} ---")
                
                try:
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "elementor-heading-title"))
                    )
                except:
                    print("Tempo esgotado ou nenhum edital encontrado nesta página.")
                    break

                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                elementos_encontrados = self.driver.find_elements(By.CSS_SELECTOR, "h2.elementor-heading-title a")
                
                print(f"Encontrados {len(elementos_encontrados)} títulos na página. Filtrando...")

                for elemento in elementos_encontrados:
                    try:
                        titulo_texto = elemento.text.strip()
                        link_url = elemento.get_attribute("href") 
                        
                        if not titulo_texto:
                            continue

                        for palavra in palavras_chave:
                            if palavra in titulo_texto.lower():
                                print(f" [MATCH] Encontrado: {titulo_texto}")
                                
                                novo_edital = Edital(titulo=titulo_texto, link=link_url)
                                editais_relevantes.append(novo_edital)
                                break 
                    except Exception as e:
                        print(f"Erro ao ler um elemento especifico: {e}")
                        continue
                
                
                try:
                    
                    botao_proximo = self.driver.find_element(By.CSS_SELECTOR, "a.next, a.page-numbers.next")
                    
                    self.driver.execute_script("arguments[0].click();", botao_proximo)
                    time.sleep(3)
                    pagina_atual += 1
                except:
                    print("Fim das páginas ou botão 'Próximo' não encontrado.")
                    break

        except Exception as error:
            print(f"Erro crítico durante o scraping: {error}")
        finally:
            self.driver.quit()
        
        return editais_relevantes