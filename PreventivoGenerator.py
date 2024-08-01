from Classes.Order import Order;
import AlmaxUtils.PdfManager as PM;
import AlmaxGraphics.FrameManager as FM;
import tkinter as TK;
import json;
from AlmaxLogs import LoggerService;
import sys,os,platform;
from tkinter import messagebox

name = "PreventivoFatturaGenerator";
window = FM.Window(name);

orders = [];
total = 0.00;
totalString = TK.StringVar(value="0,00€");
log = LoggerService(
    programNameLogger=name,
    genericLogFileName="Log.log"
);
log.Start();

def CalculateTotal(order: Order):
    global total;
    total = float(f"{(total + float(order.Total.replace(".","").replace(",", ".")))}");
    totalString.set(f"{formatFloat(total)}€")

def formatFloat(number):
    # Convert number to string and split into integer and decimal parts
    integer_part, decimal_part = f"{number:.2f}".split('.')
    # Add thousands separator
    integer_part_with_thousands = '{:,}'.format(int(integer_part)).replace(',', '.')
    # Combine integer and decimal parts with comma as decimal separator
    formatted_number = f"{integer_part_with_thousands},{decimal_part}"
    return formatted_number;

def AssignCommand(Button: TK.Button, index):
    match (index):
        case 0:
            try:
                q = float(quantity.get("1.0", TK.END).strip().replace(",", "."))
                p = float(price.get("1.0", TK.END).strip().replace(",", "."))
            except:
                messagebox.showerror(
                    "Error", "Quantità e Prezzo accettano solo numeri!"
                )
                return
            global window;
            global orders;
            global docType;

            order = Order(
                productName.get("1.0", TK.END).strip(),
                q,
                p,
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
            Button.config(text=f"Attendere..", state=TK.DISABLED)
            try:
                with open(f"{log.LogPath()}/Ordini.txt", 'r') as file:
                    data = json.load(file);
                    orders = data;
            except:
                messagebox.showerror("Error", "Il file non è generabile!");
                Button.config(text=f"Genera PDF", state=TK.NORMAL);
                return;
            newOrders = [];
            global total;
            total = 0.00;
            totalString.set("0.00€");
            for order in orders:
                newOrder = Order.FromDict(order);
                CalculateTotal(newOrder);
                newOrders.append(newOrder);
            orders = newOrders;
            totaleIva = f"{formatFloat(float(total * 0.22))}"
            totaleFinale = f"{formatFloat(float(float(total * 0.22) + total))}"
            PdfName = PM.GeneratePdf(
                clientInfo.get("1.0", TK.END).strip(),
                [order.ToDict() for order in orders],
                [
                    {"text": "TOTALE SENZA IVA", "value": f"{formatFloat(total)}€"},
                    {"text": "IVA al 22%", "value": f"{totaleIva}€"},
                    {"text": "TOTALE CON IVA", "value": f"{totaleFinale}€"},
                ],
                [f"NB: Qualsiasi modifica che non è citata, sarà pagata a parte."],
                docType.get()
            )
            log.AddLog(f"Prezzo totale: {totalString.get()}\n");
            log.AddLog(f"Stampato in {PdfName}");

            if PdfName:
                # Open the PDF file with the default PDF viewer
                if platform.system() == "Windows":
                    os.startfile(PdfName)
                elif platform.system() == "Darwin":  # macOS
                    os.system(f"open {PdfName}")
                else:  # Linux
                    os.system(f"xdg-open {PdfName}")

            Button.config(text=f"Genera di nuovo", state=TK.NORMAL);

        case 2:
            log.End();
            sys.exit(0);

def main():
    global clientInfo;
    global productName; 
    global quantity; 
    global price;
    global docType;

    window.AddFrame("DocType", TK.NW);
    window.AddLabelToFrame("Tipo di Documento", "DocType", TK.LEFT);
    docType = window.AddOptionButtonToFrame(["Documento", "Preventivo", "Fattura"], "DocType", TK.LEFT);

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
