import tkinter as tk
from tkinter import messagebox
class Item:
    def __init__(self,name,type,price,discount):
        self.name=name
        self.type=type
        self.price=price
        self.discount=discount

    def discount_value(self):        
        return self.price*(self.discount/100)

    def price_after_discount(self):
        return self.price-(self.discount_value())    



class ShowRoomApp:
    def __init__(self):
       self.frame=tk.Tk()
       self.frame.geometry("500x500")
       self.frame.title("Show Room App")    

       label=tk.Label(self.frame,text="select item")
       label.pack()

       self.items=[
            Item("TV", "32 Inch", 2300, 10),
            Item("TV", "43 Inch", 33000, 15),
            Item("TV", "55 Inch", 4300, 20),         
            Item("Refrigerator", "8 Foot", 5300, 10),
            Item("Refrigerator", "16 Foot", 9300, 15),
            Item("Refrigerator", "21 Foot", 20300, 10),
            Item("Air Condition", "1.5 HP", 14300, 15),
            Item("Air Condition", "2 HP", 17300, 10),
            Item("Air Condition", "3 HP", 23000, 17)
       ]
       self.selected_item=tk.StringVar()
       self.selected_item.set(f"{self.items[0].name}-{self.items[0].type}")
       self.menue=tk.OptionMenu(self.frame,self.selected_item,*[item.name +"-"+item.type for item in self.items])
       self.menue.pack()
 
       self.button=tk.Button(text="show invoice",command=self.get_invoice)
       self.button.pack()
       self.frame.mainloop()

    def get_invoice(self):
        selected=self.selected_item.get()
        for item in self.items:
            if item.name+"-"+item.type==selected:
                    a=(f"""
name: {item.name+"-" +item.type}
price:{item.price}
price after discount: {item.price_after_discount()}
            """)
                    messagebox.showinfo("invoice",a)
                    break

