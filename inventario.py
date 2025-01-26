class Inventario:
    def __init__(self, paginas=3, slots_por_pagina=20):
        self.paginas = paginas
        self.slots_por_pagina = slots_por_pagina
        self.slots = {pagina: [None] * slots_por_pagina for pagina in range(1, paginas + 1)}

    def listar_slots(self):
        for pagina, slots in self.slots.items():
            print(f"Página {pagina}:")
            for i, slot in enumerate(slots):
                if slot:
                    print(f"  Slot {i + 1}: {slot.nome} (x{slot.quantidade})")
                else:
                    print(f"  Slot {i + 1}: [Vazio]")
            print()


class Item:
    def __init__(self, nome, descricao, quantidade, valor_gold, trocavel=True):
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.valor_gold = valor_gold
        self.trocavel = trocavel


class ItemEquipavel(Item):
    def __init__(self, nome, descricao, quantidade, valor_gold, trocavel, tipo, dano, level_requerido, classe_requerida, nivel_fortificacao=0, efeitos_adicionais=None):
        super().__init__(nome, descricao, quantidade, valor_gold, trocavel)
        self.tipo = tipo
        self.dano = dano
        self.level_requerido = level_requerido
        self.classe_requerida = classe_requerida
        self.nivel_fortificacao = nivel_fortificacao
        self.efeitos_adicionais = efeitos_adicionais if efeitos_adicionais else []


class ItemDiverso(Item):
    def __init__(self, nome, descricao, quantidade, valor_gold, trocavel, tipo, efeito=None):
        super().__init__(nome, descricao, quantidade, valor_gold, trocavel)
        self.tipo = tipo  # "Consumível" ou "Não Consumível"
        self.efeito = efeito  # Efeito que será aplicado, se for consumível


class Descricao:
    def __init__(self, callback):
        self.callback = callback

    def enviar_descricao(self, item):
        if item:
            descricao = (
                f"Nome: {item.nome}\n"
                f"Descrição: {item.descricao}\n"
                f"Quantidade: {item.quantidade}\n"
                f"Valor em Ouro: {item.valor_gold}\n"
                f"Trocável: {'Sim' if item.trocavel else 'Não'}\n"
            )
            if isinstance(item, ItemEquipavel):
                descricao += (
                    f"Tipo: {item.tipo}\n"
                    f"Dano: {item.dano}\n"
                    f"Nível Requerido: {item.level_requerido}\n"
                    f"Classe Requerida: {item.classe_requerida}\n"
                    f"Nível de Fortificação: {item.nivel_fortificacao}\n"
                    f"Efeitos Adicionais: {', '.join(item.efeitos_adicionais)}\n"
                )
            elif isinstance(item, ItemDiverso):
                descricao += (
                    f"Tipo: {item.tipo}\n"
                    f"Efeito: {item.efeito}\n"
                )
        else:
            descricao = "Nenhum item selecionado."
        self.callback(descricao)

class Fortalecimento:
    def calcular_atributos_fortalecimento(self, item, nivel_fortalecimento):
        if isinstance(item, ItemEquipavel):
            multiplicador = 1 + (0.1 * nivel_fortalecimento)
            atributos = {
                "dano": int(item.dano * multiplicador),
                "level_requerido": item.level_requerido,
                "classe_requerida": item.classe_requerida,
                "nivel_fortificacao": nivel_fortalecimento,
                "efeitos_adicionais": item.efeitos_adicionais,
            }
            return atributos
        else:
            return "Itens consumíveis ou não equipáveis não podem ser fortalecidos."


class Fortalecimento:
    def calcular_atributos_fortalecimento(self, item):
        if isinstance(item, ItemEquipavel):
            niveis = {}
            for nivel in range(1, 16):  # 15 níveis
                multiplicador = 1 + (0.1 * nivel)
                niveis[f"Level +{nivel}"] = {
                    "dano": int(item.dano * multiplicador),
                    "level_requerido": item.level_requerido,
                    "classe_requerida": item.classe_requerida,
                    "nivel_fortificacao": nivel,
                    "efeitos_adicionais": item.efeitos_adicionais,
                }
            return niveis
        else:
            return "Itens consumíveis ou não equipáveis não podem ser fortalecidos."


