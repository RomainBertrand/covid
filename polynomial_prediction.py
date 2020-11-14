import numpy as np
import matplotlib
import data_analysis


def polynomial_prediction(csv_file, predict_until="2020-11-30"):
    dates, cases, deaths = data_analysis.analysis(csv_file, True)
    model = np.poly1d(np.polyfit(dates, cases, 5))
    x = np.linspace(
        min(dates), data_analysis.matplotlib.dates.datestr2num(predict_until))
    matplotlib.pyplot.plot(x, model(x))
    matplotlib.pyplot.show()


if __name__ == '__main__':
    polynomial_prediction("./France_data.csv")  # prediction explodes, coherent
    polynomial_prediction("./United_States_of_America_data.csv")
