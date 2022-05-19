import matplotlib.pylab as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

pyeong = 3.3058


def main():
    xlsx = pd.read_excel('./data.xlsx', 'Sheet3')

    a_size, a_price = get_data(xlsx)

    model = LinearRegression()
    model.fit(a_size, a_price)

    test_size = get_test_size()

    plt.scatter(a_size, a_price, color='black')

    pred_price = model.predict(test_size)

    plt.plot(test_size, pred_price, color='blue', linewidth=3)
    plt.show()

    for i in range(len(test_size)):
        print(f'{int(test_size[i][0] / pyeong)}평 예상 가격: {round(pred_price[i], 2)}억 원')


def get_data(xlsx):
    a_size = []
    a_price = []
    for row in xlsx.values:
        a_size.append([row[0]])
        a_price.append(row[1])
    return a_size, a_price


def get_test_size():
    return [[s * pyeong] for s in [14, 17, 21, 24, 27, 32, 34, 40]]


if __name__ == '__main__':
    main()
