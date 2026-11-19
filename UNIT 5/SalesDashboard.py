
import pandas as pd
import matplotlib.pyplot as plt

class SalesDashboard:

    def __init__(self, filename):
        self.filename = filename
        self.data: pd.DataFrame | None = None

    # Read CSV file
    def load_data(self):
        self.data = pd.read_csv(self.filename)
        print("Sales Data Loaded Successfully!")

    # Safely get loaded data
    def get_data(self) -> pd.DataFrame:
        if self.data is None:
            raise RuntimeError("Sales data has not been loaded.")
        return self.data

    # Display sales data
    def display_data(self):
        data = self.get_data()
        print("\nRetail Sales Data:")
        print(data)

    # Line graph
    def line_graph(self):
        data = self.get_data()
        data["Date"] = pd.to_datetime(data["Date"])

        daily_sales = data.groupby("Date")["Sales"].sum()

        plt.plot(daily_sales.index, daily_sales.to_numpy(dtype=float),
                 marker='o')

        plt.title("Daily Retail Sales")
        plt.xlabel("Date")
        plt.ylabel("Sales")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # Bar chart
    def bar_chart(self):
        data = self.get_data()
        product_sales = data.groupby("Product")["Sales"].sum()

        plt.bar(product_sales.index, product_sales.to_numpy(dtype=float))

        plt.title("Product-wise Sales")
        plt.xlabel("Product")
        plt.ylabel("Total Sales")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


# Create object
dashboard = SalesDashboard("sales.csv")

# Call methods
dashboard.load_data()
dashboard.display_data()
dashboard.line_graph()
dashboard.bar_chart()
