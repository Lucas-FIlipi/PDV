import re

def buscar_item(lista_skus, plu="plu.txt"):
    resultados = []
    
    with open(plu, "r", encoding="utf-8") as f:
        for linha in f:
            partes = linha.strip().split("|")
            
            if len(partes) > 9:
                
                try: #faz em 2 em 2
                    item = {
                        "name": partes[1],
                        "value": float(partes[3]),
                        "tax": partes[5],
                        "ID": partes[7],
                        "SKU": partes[9],
                    }
                except ValueError:
                    continue 

                for sku_busca in lista_skus:
                    if re.search(sku_busca, item["SKU"], re.IGNORECASE):
                        resultados.append(item)
                    else:
                        print(f"AVISO: O SKU {sku_busca} não foi encontrado.")
                        return None
                    break
    return resultados