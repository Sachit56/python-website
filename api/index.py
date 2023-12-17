

from taipy import Gui
import pandas as pd

data = {
    "Date": pd.date_range("2023-04-12", periods=4, freq="D"),
    "Min": [-22, -19.7, 2.7, 6.5],
    "Max": [-8.6, -8.2, 12., 13.5]
}

title = "Real State Simulator using python"
logo = "logo.jpeg"
plot_location = 'Bhaktapur'
plot_max_price = 500000000
plot_min_price = 100000000

def run(state):
    print(f'{plot_max_price} is maximum.')

    print(state.plot_location)

    with open("data.txt","a") as f:
        f.write(f'\n{state.plot_location},{state.plot_max_price},{state.plot_min_price}')



page = """
<| text-center
<|{logo}|image|>

<|{title}|>

Location of Plot:<|{plot_location}|input|>

Maximum Price:<|{plot_max_price}|number|>

Minimum Price:<|{plot_min_price}|number|>

<|Submit|button|on_action=run|>

<|{data}|chart|mode=lines|x=Date|y[1]=Min|y[2]=Max|line[1]=dash|color[2]=blue|>

|>
"""

if __name__ == "__main__":
    app = Gui(page)
    app.run(use_reloader=True)
