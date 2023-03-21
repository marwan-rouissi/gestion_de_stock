import tkinter as tk
from tkinter import *
from produit import *
from tkinter import ttk
import matplotlib.pyplot as plt

class App:
    # création d'un objet App (menu principal)
    def __init__(self):
        #
        self.gui = Tk()
        self.gui.geometry("400x380")
        self.gui.title("Boutique")
        # variable d'instance de la classe Produit
        self.Quantite = Produit()
        # Txt 
        Boutique_label = tk.Label(self.gui, text="Ma\nBoutique",foreground="blue", font=5)
        Boutique_label.pack(pady=50)
        # boutons
        check_btn = tk.Button(self.gui, text="Voir produits", borderwidth=10, command=self.displayProd)
        check_btn.pack(pady=5)
        #
        AddProd_btn = tk.Button(self.gui, text="Ajouter Produit", borderwidth=10, command=self.openAddProd)
        AddProd_btn.pack(pady=5)
        #
        ModProd_btn = tk.Button(self.gui, text="Modifier Produit", borderwidth=10, command=self.updateProd)
        ModProd_btn.pack(pady=5)
        #
        DelProd_btn = tk.Button(self.gui, text="Supprimer Produit", borderwidth=10, command=self.deleteProd)
        DelProd_btn.pack(pady=5)

        self.gui.mainloop()
        # fermeture du curseur une fois l'application fermée 
        self.Quantite.cursor.close()
        print("curseur fermé")

    # méthode pour ouvrir et afficher le TopLvl contenant mes produits
    def displayProd(self):
        prod = tk.Toplevel(self.gui)
        prod.title("Mes Produits")
        prod.geometry("1250x600")

        col = ("ID", "Produit", "Desc", "Prix", "Quantite", "categorie")

        tree = ttk.Treeview(prod, columns=col, show="headings")

        tree.heading("ID", text="ID")
        tree.heading("Produit", text="Produit")
        tree.heading("Desc", text="Desc")
        tree.heading("Prix", text="Prix")
        tree.heading("Quantite", text="Quantite")
        tree.heading("categorie", text="categorie")

        items = self.Quantite.displayDATA()

        for item in items:
            tree.insert("", tk.END, values=item)
        
        tree.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(prod, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1)
        #
        Export_btn = tk.Button(prod, text="Export CSV", borderwidth=10, command=self.Quantite.exportCSV)
        Export_btn.grid(row=1, column=0, pady=5)
        #
        graph_btn = tk.Button(prod, text="voir Stock", borderwidth=10, command=self.graphQuantite)
        graph_btn.grid(row=1, column=0, pady=5, sticky="w")
        self.L = self.Quantite.displayCat()
        var = tk.Variable(value=self.L)

        self.QuantiteList = tk.Listbox(prod, listvariable=var, height=10, selectmode=tk.SINGLE)
        self.QuantiteList.grid(column=0, row=2, pady=20)
        #
        Export_btn = tk.Button(prod, text="Export CSV", borderwidth=10, command=lambda : self.Quantite.filtredCSV(self.getSelectedItem()))
        Export_btn.grid(row=3, column=0, pady=5)

        prod.mainloop()

    # méthode pour ouvrir et afficher ma fenêtre permettant l'ajout d'un nouveau produit
    def openAddProd(self):
        #
        self.addProd = tk.Toplevel(self.gui)
        #
        self.addProd.title("Ajouter produit")
        #
        self.addProd.geometry("500x300")
        #
        page_Label = tk.Label(self.addProd, text="Produit à ajouter:",foreground="black", font=5, pady=20)
        page_Label.grid(column=0, row=0)
        # Infos du produit à ajouter
        nomProd_Label = tk.Label(self.addProd, text="Nom:",foreground="black", font=5)
        nomProd_Label.grid(column=0, row=1)
        #
        self.nomProd_Entry = tk.Entry(self.addProd, width=30)
        self.nomProd_Entry.grid(column=1, row=1)
        #
        descrProd_Label = tk.Label(self.addProd, text="Description:",foreground="black", font=5)
        descrProd_Label.grid(column=0, row=2)
        #
        self.descProd_Entry = tk.Entry(self.addProd, width=30)
        self.descProd_Entry.grid(column=1, row=2)
        #
        prixProd_Label = tk.Label(self.addProd, text="Prix:",foreground="black", font=5)
        prixProd_Label.grid(column=0, row=3)
        #
        self.prixProd_Entry = tk.Entry(self.addProd, width=30)
        self.prixProd_Entry.grid(column=1, row=3)
        #
        QuantiteProd_Label = tk.Label(self.addProd, text="Quantite:",foreground="black", font=5)
        QuantiteProd_Label.grid(column=0, row=4)
        #
        self.QuantiteProd_Entry = tk.Entry(self.addProd, width=30)
        self.QuantiteProd_Entry.grid(column=1, row=4)
        #
        catProd_Label = tk.Label(self.addProd, text="id_Categorie:",foreground="black", font=5)
        catProd_Label.grid(column=0, row=5)
        #
        self.catProd_Entry = tk.Entry(self.addProd, width=30)
        self.catProd_Entry.grid(column=1, row=5)
        #
        Submit_btn = tk.Button(self.addProd, text="Ajouter", borderwidth=10, command=lambda : self.Quantite.addProd(self.getNom(), self.getDesc(), self.getPrix(), self.getQuantite(), self.getCat(), self.addProd))
        Submit_btn.grid(column=1, row=6, pady=20)

    # méthode pour ouvrir et afficher ma fenêtre permettant la modification d'un de mes produits
    def updateProd(self):
        #
        updProd = tk.Toplevel(self.gui)
        #
        updProd.title("Modifier produit")
        #
        updProd.geometry("500x500")
        #
        self.L = self.Quantite.displayProd()
        var = tk.Variable(value=self.L)

        self.QuantiteList = tk.Listbox(updProd, listvariable=var, height=10, selectmode=tk.SINGLE)
        self.QuantiteList.grid(column=1, row=0)
        page_Label = tk.Label(updProd, text="Produit à modifier:",foreground="black", font=5, pady=20)
        page_Label.grid(column=0, row=0)

        # Infos du produit à modifier 
        nomProd_Label = tk.Label(updProd, text="Nom:",foreground="black", font=5)
        nomProd_Label.grid(column=0, row=1)
        #
        self.nomProd_Entry = tk.Entry(updProd, width=30)
        self.nomProd_Entry.grid(column=1, row=1)
        #
        Submit_btn = tk.Button(updProd, text="Modifier", borderwidth=10, command=lambda : self.Quantite.updateProdName(self.getSelectedItem(), self.getNom(), updProd))
        Submit_btn.grid(column=2, row=1, pady=5, padx=15)
        #
        descrProd_Label = tk.Label(updProd, text="Description:",foreground="black", font=5)
        descrProd_Label.grid(column=0, row=2)
        #
        self.descProd_Entry = tk.Entry(updProd, width=30)
        self.descProd_Entry.grid(column=1, row=2)

        #
        Submit_btn = tk.Button(updProd, text="Modifier", borderwidth=10, command=lambda : self.Quantite.updateProdDesc(self.getSelectedItem(), self.getDesc, updProd))
        Submit_btn.grid(column=2, row=2, pady=5)
        #
        prixProd_Label = tk.Label(updProd, text="Prix:",foreground="black", font=5)
        prixProd_Label.grid(column=0, row=3)
        #
        self.prixProd_Entry = tk.Entry(updProd, width=30)
        self.prixProd_Entry.grid(column=1, row=3)
        #
        Submit_btn = tk.Button(updProd, text="Modifier", borderwidth=10, command=lambda : self.Quantite.updateProdPrice(self.getSelectedItem(), self.getPrix(), updProd))
        Submit_btn.grid(column=2, row=3, pady=5)
        #
        QuantiteProd_Label = tk.Label(updProd, text="Quantite:",foreground="black", font=5)
        QuantiteProd_Label.grid(column=0, row=4)
        #
        self.QuantiteProd_Entry = tk.Entry(updProd, width=30)
        self.QuantiteProd_Entry.grid(column=1, row=4)
        #
        Submit_btn = tk.Button(updProd, text="Modifier", borderwidth=10, command=lambda : self.Quantite.updateProdStock(self.getSelectedItem(), self.getQuantite(), updProd))
        Submit_btn.grid(column=2, row=4, pady=5)
        #
        catProd_Label = tk.Label(updProd, text="id_Categorie:",foreground="black", font=5)
        catProd_Label.grid(column=0, row=5)
        #
        self.catProd_Entry = tk.Entry(updProd, width=30)
        self.catProd_Entry.grid(column=1, row=5)
        #
        Submit_btn = tk.Button(updProd, text="Modifier", borderwidth=10, command=lambda : self.Quantite.updateProdCat(self.getSelectedItem(), self.getCat(), updProd))
        Submit_btn.grid(column=2, row=5, pady=5)

    # méthode pour ouvrir et afficher ma fenêtre permettant la suppresion d'un de mes produits
    def deleteProd(self):
        #
        delProd = tk.Toplevel(self.gui)
        #
        delProd.title("Supprimer produit")
        #
        delProd.geometry("500x300")
        #
        self.L = self.Quantite.displayProd()
        var = tk.Variable(value=self.L)

        self.QuantiteList = tk.Listbox(delProd, listvariable=var, height=10, selectmode=tk.SINGLE)
        self.QuantiteList.grid(column=1, row=0)
        page_Label = tk.Label(delProd, text="Produits à supprimer:",foreground="black", font=5, pady=20)
        page_Label.grid(column=0, row=0)
        #
        Del_btn = tk.Button(delProd, text="Supprimer", borderwidth=10, command=lambda : self.Quantite.delProd(self.getSelectedItem(), delProd))
        Del_btn.grid(column=1, row=6, pady=20)

    ## mes getter 
    def getSelectedItem(self):
        return self.QuantiteList.get(ANCHOR)
    #
    def getNom(self):
        return self.nomProd_Entry.get()
    #
    def getDesc(self):
        return self.descProd_Entry.get()
    #
    def getPrix(self):
        return self.prixProd_Entry.get()
    #
    def getQuantite(self):
        return self.QuantiteProd_Entry.get()
    #
    def getCat(self):
        return self.catProd_Entry.get()

    def graphQuantite(self):
        # variable contenant mes noms de produits sous forme de liste 
        prod = self.Quantite.displayProd()
        # variable contenant mes quantites de produits sous forme de liste
        Quantite = self.Quantite.displayStock()

        # création de mon graph
        plt.pie(Quantite, labels=prod, autopct='%1.1f%%', startangle=90, shadow=True)
        plt.title("Quantite")
        plt.axis('equal')
        plt.show()

if __name__ == "__main__":
    app = App()