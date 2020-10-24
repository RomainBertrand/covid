import csv
import matplotlib
import matplotlib.pyplot as plt


def analysis(filename, return_values=False):
    dates = []
    cases = []
    deaths = []
    with open(filename, 'r') as csv_file:
        csv_lines = csv.reader(csv_file, delimiter=',')
        fields_indexes = get_csv_labels(
            next(csv_lines), ["year", "day", "month", "deaths", "cases"])
        for line in csv_lines:
            dates.append(matplotlib.dates.datestr2num(
                line[fields_indexes["year"]]+'-'+line[fields_indexes["month"]]+'-'+line[fields_indexes["day"]]))
            cases.append(int(line[fields_indexes["cases"]]))
            deaths.append(int(line[fields_indexes["deaths"]]))
    if return_values:
        return dates, cases, deaths
    plt.plot_date(dates, cases, fmt='.')
    plt.plot_date(dates, deaths, fmt='.')
    plt.show()


def get_csv_labels(first_line, fields_searched):
    index = 0
    fields_indexes = {}
    for label in first_line:
        if label in fields_searched:
            fields_indexes[label] = index
        index += 1
    return fields_indexes


if __name__ == '__main__':
    analysis("./France_data.csv")
