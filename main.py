import tkinter as tk
from tkinter import ttk
import modelo as crud

class PrincipalBD():
    def __init__(self, win):
        self.objBD = crud.AppBD()
        self.janela = win

        self.treeProdutos = ttk.Treeview(self.janela, 
                                              columns=("Código do Produto",
                                                        "Nome", 
                                                        "Preço"))
        self.treeProdutos.heading("Código do Produto", text="Código do Produto:")
        self.treeProdutos.heading("Nome", text="Nome:")
        self.treeProdutos.heading("Preço", text="Preço:")
        self.treeProdutos.pack()

        self.lblNome = tk.Label(self.janela, text="Nome:")
        self.lblNome.pack()
        self.entryNome = tk.Entry(self.janela)
        self.entryNome.pack()

        self.lblPreco = tk.Label(self.janela, text="Preço:")
        self.lblPreco.pack()
        self.entryPreco = tk.Entry(self.janela)
        self.entryPreco.pack()
self.cadrastrar = tk.button(self.janela
text="preço:")
self.iblPreço.pack()
self.entryPreco = tk.Entry(self.janela)
self.entryPreco.pack()




def ExibirTela(self):
    try:
        print("*****dados*****")
        products = self.objBD.select_all_products()
        for product in products:
            self.treeProdutos.insert("", tk.END, valoues=product)
            except:
                print ("não foi possivel exibir os campos")



def fcadrastroProduto(self):
    try
    name = self.entryMone.get()
    price = float(self.entryPreco.get())
    self.objBD.inserirDados(name,price)
    self.entryMone.delete(0, tk END)
    self.entryPreco.delete(0, tk END)
    print("produto cadrastrado")
    except Exception as error:
    print("produto não cadrastrado" ,error)


    def atualizarProduto(self)
    try:
        selectd_item = self.treeProdutos.selection()
        if not selectd_item:
            return
            iten = self.treeProdutos.item(selectd_item)
            print(item)
            product = item["values"]
            product_id = product[0]
            nome = self.entryNome.get()
            preco = float(self_entryPreco.get())
            self.objBD.update_product(product_id,nomepreco)
            self.ExibirTela()
            self.entryMone.delete(0, tk.END)
            self_entryPreco.delete(0, tk.END)
            print("produto atualizado com sucesso")
            except Exception as e:
                print("não foi possivel fazer a atualização," e)

                def delete_product(self)
                try:
                    selectd_item = self.treeProdutos.selection


janela = tk.Tk()
product_app = PrincipalBD(janela)
janela.title("Bem vindo a aplicação de banco de dados")
janela.geometry("900x700")
janela.mainloop()