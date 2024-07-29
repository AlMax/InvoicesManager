from Classes.Order import Order;
import AlmaxUtils.PdfManager as PM;
import AlmaxGraphics.FrameManager as FM;
import tkinter as TK;
import json;
from AlmaxLogs import LoggerService;
import sys;

name = "PreventivoGenerator";
window = FM.Window(name);

orders = [];
total = 0.00;
totalString = TK.StringVar(value="0.00€");
log = LoggerService(
    programNameLogger=name,
    genericLogFileName="Log.log"
);
log.Start();

def CalculateTotal(order: Order):
    global total;
    total = float(f"{(float(total) + float(order.Total.replace(",", ""))):.2f}");
    totalString.set(f"{total}€");

def AssignCommand(Button: TK.Button, index):
    match (index):
        case 0:
            global window
            global orders

            order = Order(
                productName.get("1.0", TK.END).strip(),
                float(quantity.get("1.0", TK.END).strip().replace(",", ".")),
                float(price.get("1.0", TK.END).strip().replace(",", ".")),
            )
            log.AddLog("Aggiunto un ordine")
            log.AddLog(f"\t{order.ToDict()}\n")
            orders.append(order)

            CalculateTotal(order)

            with open(f"{log.LogPath()}/Ordini.txt", "w") as file:
                json.dump([obj.ToDict() for obj in orders], file)

            productName.delete("1.0", TK.END)
            quantity.delete("1.0", TK.END)
            price.delete("1.0", TK.END)

        case 1:
            with open(f"{log.LogPath()}/Ordini.txt", 'r') as file:
                data = json.load(file);
                orders = data;
            newOrders = [];
            global total;
            total = 0.00;
            totalString.set("0.00€");
            for order in orders:
                newOrder = Order.FromDict(order);
                CalculateTotal(newOrder);
                newOrders.append(newOrder);
            orders = newOrders;
            PdfName = PM.GeneratePdf(
                clientInfo.get("1.0", TK.END).strip(),
                [order.ToDict() for order in orders],
            );
            log.AddLog(f"Prezzo totale: {totalString.get()}\n");
            log.AddLog(f"Stampato in {PdfName}");

        case 2:
            log.End();
            sys.exit(0);

def main():
    global clientInfo;
    global productName; 
    global quantity; 
    global price;

    window.AddFrame("ClientName", TK.NW);
    window.AddLabelToFrame("Inserire il Cliente", "ClientName", TK.LEFT);
    clientInfo = window.AddTextToFrame("ClientName", TK.LEFT)

    window.AddFrame("Product", TK.NW);
    window.AddLabelToFrame("Prodotto", "Product", TK.LEFT);
    productName = window.AddTextToFrame("Product", TK.LEFT)

    window.AddFrame("Quantity", TK.NW);
    window.AddLabelToFrame("Quantità", "Quantity", TK.LEFT);
    quantity = window.AddTextToFrame("Quantity", TK.LEFT)

    window.AddFrame("Price", TK.NW);
    window.AddLabelToFrame("Prezzo", "Price", TK.LEFT);
    price = window.AddTextToFrame("Price", TK.LEFT)

    window.AddFrame("Data", TK.NW);
    window.AddLabelToFrame("Prezzo Totale senza IVA", "Data", TK.LEFT);
    window.AddLabelToFrame(f"", "Data", TK.LEFT).config(textvariable=totalString)

    window.AddFrame("Buttons", TK.S);
    window.AddButtonToFrame("Aggiungi", 0, AssignCommand, "Buttons", TK.LEFT)
    window.AddButtonToFrame("Genera PDF", 1, AssignCommand, "Buttons", TK.LEFT)
    window.AddButtonToFrame("Chiudi", 2, AssignCommand, "Buttons", TK.LEFT)

    window.Mainloop();


if __name__ == "__main__":
    main();

    if False:
        client_info = {
            "name": "Ali Srls"
        };
        orders = [
            Order('fbewkjfbwebfjewbfkjewbfkewfewfvjewbfjwebfjkewjfbewfjwebjfwejfjwebfjewbfjwefwebfwefweeffwe', 2.6, 31.5),
            Order('ciao', 2.6, 34090.5),
            Order('fbewkjfbwebfjewbfkjewbfkewfewfvjewbfjwebfjkewjfbewfjwebjfwejfjwebfjewbfjwefwebfwefweeffwe', 2.6, 32.5),
            Order('fbewkjfbwebfjewbfkjewbfkewfewfvjewbfjwebfjkewjfbewfjwebjfwejfjwebfjewbfjwefwebfwefweeffwe', 2.6, 33.5),
            Order('fbewkjfbwebfjewbfkjewbfkewfewfvjewbfjwebfjkewjfbewfjwebjfwejfjwebfjewbfjwefwebfwefweeffwe', 2.6, 34.5)
        ];

        PM.GeneratePdf(client_info, Order, orders);
