import mysql.connector
from tkinter import messagebox
import csv

class Produit:

    def __init__(self) -> None:
        # ma base de donnee
        self.bd = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "Bl@ckbird772",
            database = "boutique"
        )
        # création d'un curseur
        self.cursor = self.bd.cursor()
        
        # nom de la table à modifier
        self.tableProd = "produits"
        self.tableCat = "categories"

    # méthode pour ajouter un nouveau produit à la bdd
    def addProd(self, nom, description, prix, quantite, id_categorie, tl):
        # requete
        req = f"""insert into {self.tableProd} (nom, description, prix, quantite, id_categorie) \
            values \
            ("{nom}", "{description}", {prix}, "{quantite}", "{id_categorie}");"""

        try:
            # execution de ma requête
            self.cursor.execute(req)

            # appliquer l'ajout de maniere permanente
            self.bd.commit()

            messagebox.showinfo("Info", message=f"Le produit: {nom} a été ajouté au stock.")
            
            # fermeture de la fenêtre Tk
            tl.destroy()

        except:
            messagebox.showerror("Erreur", message="Un (ou plusieurs) champs non renseigné(s).\nVeuillez réessayer.")

        # print(nom, description, prix)

    # méthode pour supprimer un produit
    def delProd(self, itemToDelete, tl):
        # requete
        req = f"""delete from {self.tableProd} where nom = "{itemToDelete}";"""

        # execution de ma requête
        self.cursor.execute(req)

        # appliquer l'ajout de maniere permanente
        self.bd.commit()

        messagebox.showinfo("Info", message=f"{itemToDelete} a été supprimé du stock.")

        # fermeture de la fenêtre Tk
        tl.destroy()
    
    # méthode pour modifier le nom d'un produit
    def updateProdName(self, actualName, newName, tl):
        # requete
        req = f"""update {self.tableProd} \
            set nom = '{newName}'\
            where nom = "{actualName}" ;"""

        # execution de ma requête
        self.cursor.execute(req)

        # appliquer l'ajout de maniere permanente
        self.bd.commit()
        messagebox.showinfo("Info", message=f"Le nom du produit: {actualName} a été modifié.")

        # fermeture de la fenêtre Tk
        tl.destroy()

    # méthode pour modifier la description d'un produit
    def updateProdDesc(self, actualName, newDesc, tl):
        # requete
        req = f"""update {self.tableProd} \
            set description = {newDesc}\
            where nom = "{actualName}" ;"""

        # execution de ma requête
        self.cursor.execute(req)

        # appliquer l'ajout de maniere permanente
        self.bd.commit()
        messagebox.showinfo("Info", message=f" La description du produit: {actualName} a été modifiée.")
        
        # fermeture de la fenêtre Tk
        tl.destroy()

    # méthode pour modifier le prix d'un produit
    def updateProdPrice(self, actualName, newPrice, tl):
        # requete
        req = f"""update {self.tableProd} \
            set prix = {newPrice}\
            where nom = "{actualName}" ;"""

        # execution de ma requête
        self.cursor.execute(req)

        # appliquer l'ajout de maniere permanente
        self.bd.commit()
        messagebox.showinfo("Info", message=f"Le prix du produit: {actualName} a été modifié.")
        
        # fermeture de la fenêtre Tk
        tl.destroy()

    # méthode pour modifier la quantite d'un produit
    def updateProdStock(self, actualName, newStock, tl):
        # requete
        req = f"""update {self.tableProd} \
            set quantite = {newStock}\
            where nom = "{actualName}" ;"""

        # execution de ma requête
        self.cursor.execute(req)

        # appliquer l'ajout de maniere permanente
        self.bd.commit()
        messagebox.showinfo("Info", message=f"La quantite du produit: {actualName} a été modifié.")
        
        # fermeture de la fenêtre Tk
        tl.destroy()

    # méthode pour modifier la catégorie d'un produit
    def updateProdCat(self, actualName, newCat, tl):
        # requete
        req = f"""update {self.tableProd} \
            set id_categorie = {newCat}\
            where nom = "{actualName}" ;"""

        # execution de ma requête
        self.cursor.execute(req)

        # appliquer l'ajout de maniere permanente
        self.bd.commit()
        messagebox.showinfo("Info", message=f"La catégorie du produit: {actualName} modifiée.")
        
        # fermeture de la fenêtre Tk
        tl.destroy()

    # méthode pour récuperer les nom de produits (pour mes listBox)
    def displayProd(self):
        # requete
        req = f"""select * from {self.tableProd};"""

        # execution de ma requête
        self.cursor.execute(req)

        self.data = self.cursor.fetchall()

        produit = []

        for element in self.data:
            produit.append(element[1])

        return produit
    
    # méthode pour récuperer les quantite de produits (pour mon graph)
    def displayStock(self):
        # requete
        req = f"""select * from {self.tableProd};"""

        # execution de ma requête
        self.cursor.execute(req)

        self.data = self.cursor.fetchall()

        stock = []

        for element in self.data:
            stock.append(element[4])

        return stock

    # méthode pour récupérer mes data (id, nom, descr, prix, quantite, catégorie)
    def displayDATA(self):
        # requete
        req = f"""select produits.id, produits.nom, description, prix, quantite, categories.nom \
            from {self.tableProd} inner join categories on produits.id_categorie = categories.id;"""

        # execution de ma requête
        self.cursor.execute(req)

        rows = self.cursor.fetchall()

        itemList = []
        for row in rows:
            itemList.append(row)

        return itemList
    
    # méthode pour récuprérer mes catégories (pour ma listBox filtre)
    def displayCat(self):
        # requete
        req = f"""select * from {self.tableCat};"""

        # execution de ma requête
        self.cursor.execute(req)

        self.data = self.cursor.fetchall()

        produit = []

        for element in self.data:
            produit.append(element[1])

        return produit

    # méthode pour exporter tout mon stock en fichier .csv
    def exportCSV(self):
        # requete
        req = f"""select produits.id, produits.nom, description, prix, quantite, categories.nom \
            from {self.tableProd} inner join categories on produits.id_categorie = categories.id;"""

        # execution de ma requête
        self.cursor.execute(req)

        data_dict = self.cursor.fetchall()

        with open("stockComplet.csv", "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter=";")
            w.writerow([i[0] for i in self.cursor.description])
            w.writerows(data_dict)
            f.close()
        
        messagebox.showinfo("Info", message="Stock exporté dans stockComplet.csv")

    # méthode pour exporter la catégorie choisie en fichier .csv
    def filtredCSV(self, selectedCat):
        # requete
        req = f"""select produits.id, produits.nom, description, prix, quantite, categories.nom \
            from {self.tableProd} inner join categories on produits.id_categorie = categories.id \
                where categories.nom = "{selectedCat}";"""

        # execution de ma requête
        self.cursor.execute(req)

        data_dict = self.cursor.fetchall()

        with open(f"{selectedCat}.csv", "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter=";")
            w.writerow([i[0] for i in self.cursor.description])
            w.writerows(data_dict)
            f.close()
        
        messagebox.showinfo("Info", message=f"Catégorie: {selectedCat} exportée dans {selectedCat}.csv")