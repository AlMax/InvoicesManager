import Order;
from Utils import FileSystem;

def main():
    client_info = {
        "name": "Ali Srls"
    };
Utils.
    orders = [
        Order('fbewkjfbwebfjewbfkjewbfkewfewfvjewbfjwebfjkewjfbewfjwebjfwejfjwebfjewbfjwefwebfwefweeffwe', 2.6, 34.5),
        Order('ciao', 2.6, 34090.5),
        Order('fbewkjfbwebfjewbfkjewbfkewfewfvjewbfjwebfjkewjfbewfjwebjfwejfjwebfjewbfjwefwebfwefweeffwe', 2.6, 34.5),
        Order('fbewkjfbwebfjewbfkjewbfkewfewfvjewbfjwebfjkewjfbewfjwebjfwejfjwebfjewbfjwefwebfwefweeffwe', 2.6, 34.5),
        Order('fbewkjfbwebfjewbfkjewbfkewfewfvjewbfjwebfjkewjfbewfjwebjfwejfjwebfjewbfjwefwebfwefweeffwe', 2.6, 34.5)
    ];

    PdfGenerator(client_info, orders);

if __name__ == "__main__":
    main();