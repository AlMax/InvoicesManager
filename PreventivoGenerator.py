from Classes.Order import Order;
import AlmaxUtils.PdfManager as PM;

def main():
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

if __name__ == "__main__":
    main();