import tkinter as tk

class EquipamentoGUI:
    def __init__(self, master):
        self.master = master
        frame = tk.Frame(master)
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Equipamento").pack()
        # Verificar se `master` é uma janela principal (Tk) ou um Frame
        if isinstance(master, tk.Tk):
            self.master.title("Equipamento do Jogador")
            self.master.geometry("600x600")

        # Informações do Jogador
        self.player_frame = tk.Frame(self.master)
        self.player_frame.pack(pady=10)

        self.player_name_label = tk.Label(self.player_frame, text="Nome do Jogador: Hikaros", font=("Arial", 12, "bold"))
        self.player_name_label.grid(row=0, column=0, sticky="w", padx=10)

        self.kills_label = tk.Label(self.player_frame, text="Kills: 50", font=("Arial", 10))
        self.kills_label.grid(row=1, column=0, sticky="w", padx=10)

        self.deaths_label = tk.Label(self.player_frame, text="Mortes: 20", font=("Arial", 10))
        self.deaths_label.grid(row=2, column=0, sticky="w", padx=10)

        self.kdr_label = tk.Label(self.player_frame, text="KDR: 250%", font=("Arial", 10))
        self.kdr_label.grid(row=3, column=0, sticky="w", padx=10)

        # Slots para equipamentos
        self.slots_frame = tk.Frame(self.master)
        self.slots_frame.pack(pady=10)

        self.slots = {
            "Capacete": tk.Button(self.slots_frame, text="Capacete", width=12, height=2),
            "Peitoral": tk.Button(self.slots_frame, text="Peitoral", width=12, height=2),
            "Luvas": tk.Button(self.slots_frame, text="Luvas", width=12, height=2),
            "Botas": tk.Button(self.slots_frame, text="Botas", width=12, height=2),
            "Espada": tk.Button(self.slots_frame, text="Espada", width=12, height=2),
            "Acessório 1": tk.Button(self.slots_frame, text="Acessório 1", width=12, height=2),
            "Acessório 2": tk.Button(self.slots_frame, text="Acessório 2", width=12, height=2),
            "Acessório 3": tk.Button(self.slots_frame, text="Acessório 3", width=12, height=2),
            "Acessório 4": tk.Button(self.slots_frame, text="Acessório 4", width=12, height=2),
            "Mascote": tk.Button(self.slots_frame, text="Mascote", width=12, height=2),
        }

        # Organizando os slots em uma grade
        self.slots["Capacete"].grid(row=0, column=1, padx=5, pady=5)
        self.slots["Peitoral"].grid(row=1, column=1, padx=5, pady=5)
        self.slots["Luvas"].grid(row=1, column=0, padx=5, pady=5)
        self.slots["Botas"].grid(row=2, column=1, padx=5, pady=5)
        self.slots["Espada"].grid(row=1, column=2, padx=5, pady=5)

        self.slots["Acessório 1"].grid(row=0, column=3, padx=5, pady=5)
        self.slots["Acessório 2"].grid(row=1, column=3, padx=5, pady=5)
        self.slots["Acessório 3"].grid(row=2, column=3, padx=5, pady=5)
        self.slots["Acessório 4"].grid(row=3, column=3, padx=5, pady=5)

        self.slots["Mascote"].grid(row=3, column=1, padx=5, pady=5)

        # Informações de Status do Jogador
        self.status_frame = tk.Frame(self.master)
        self.status_frame.pack(pady=20)

        self.status_labels = {
            "Dano Físico": tk.Label(self.status_frame, text="Dano Físico: 0", anchor="w"),
            "Dano Mágico": tk.Label(self.status_frame, text="Dano Mágico: 0", anchor="w"),
            "Defesa Física": tk.Label(self.status_frame, text="Defesa Física: 0", anchor="w"),
            "Defesa Mágica": tk.Label(self.status_frame, text="Defesa Mágica: 0", anchor="w"),
            "Velocidade": tk.Label(self.status_frame, text="Velocidade: 0", anchor="w"),
            "Crítico": tk.Label(self.status_frame, text="Crítico: 0%", anchor="w"),
        }

        for i, (status, label) in enumerate(self.status_labels.items()):
            label.grid(row=i, column=0, sticky="w", padx=10, pady=2)

        # Botão para atualizar status
        self.update_button = tk.Button(self.master, text="Atualizar Status", command=self.atualizar_status)
        self.update_button.pack(pady=10)

    def atualizar_status(self):
        self.status_labels["Dano Físico"].config(text="Dano Físico: 350")
        self.status_labels["Dano Mágico"].config(text="Dano Mágico: 200")
        self.status_labels["Defesa Física"].config(text="Defesa Física: 1800")
        self.status_labels["Defesa Mágica"].config(text="Defesa Mágica: 1500")
        self.status_labels["Velocidade"].config(text="Velocidade: 60")
        self.status_labels["Crítico"].config(text="Crítico: 15%")
        self.atualizar_kdr(50, 20)  # Simulação de kills e mortes

    def atualizar_kdr(self, kills, deaths):
        kdr = (kills / deaths) * 100 if deaths > 0 else 0
        self.kills_label.config(text=f"Kills: {kills}")
        self.deaths_label.config(text=f"Mortes: {deaths}")
        self.kdr_label.config(text=f"KDR: {kdr:.2f}%")


if __name__ == "__main__":
    root = tk.Tk()
    gui = EquipamentoGUI(root)
    root.mainloop()
