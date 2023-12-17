# from taipy import Gui
# import pandas as pd


# data = {
#           "Date": pd.date_range("2023-04-12", periods=100, freq="D"),
#           "Temp°C": [-15,-12.9,7.2,10.2],
#           "Min": [-22,-19.7,2.7,6.5],
#           "Max": [-8.6,-8.2,12.,13.5]

#   }

# title="Real State Simulator using python"
# logo="logo.jpeg"
# plot_location='Bhaktapur'
# plot_max_price=5000000
# plot_min_price=1000000
# page="""

# <| text-center
# <|{logo}|image|>

# <|{title}|>

# Location of Plot:<|{plot_location}|input|>

# Maximum Price:<|{plot_max_price}|number|>

# Minimum Plot:<|{plot_min_price}|number|>

# <|{data}|chart|mode=lines|x=Date|y[1]=Temp°C|y[2]=Min|y[3]=Max|line[1]=dash|color[2]=blue|color[3]=red|>

# |>
# """

# if __name__=="__main__":
#     app=Gui(page)
#     app.run(use_reloader=True)

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
plot_max_price = 5000000
plot_min_price = 1000000
page = """
<| text-center
<|{logo}|image|>

<|{title}|>

Location of Plot:<|{plot_location}|input|>

Maximum Price:<|{plot_max_price}|number|>

Minimum Plot:<|{plot_min_price}|number|>

<|{data}|chart|mode=lines|x=Date|y[1]=Min|y[2]=Max|line[1]=dash|color[2]=blue|>

|>
"""

if __name__ == "__main__":
    app = Gui(page)
    app.run(use_reloader=True)
