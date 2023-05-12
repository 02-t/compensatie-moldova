import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import locale

locale.setlocale(locale.LC_ALL, '')


def format_tick(value, _):
    return '{:,.0f}'.format(value)


def run_chart():
    df = pd.read_csv('data.csv')
    df = df.dropna()

    title_x = "VDAE (venitul disponibil pentru achitarea energiei)"
    title_y = "CERPA (costul energiei in perioada rece a anului)"

    max_x = 100000
    max_y = 20000

    df['VDAE'] = ((df['VGL'] - df['MCF'] - df['RLCI']) / max_x) * 100
    df['CERPA'] = (df['CERPA'] / max_y) * 100

    sns.set_style('whitegrid')
    sns.scatterplot(data=df, x='VDAE', y='CERPA', color='red')


    plt.title("Raportul dintre cheltuielile pentru resursele energetice si venitul disponibil pentru achitarea energiei")
    plt.ylabel(title_y)
    plt.xlabel(title_x)

    plt.xlim(0, 100)
    plt.ylim(0, 100)

    plt.gca().xaxis.set_major_formatter(ticker.PercentFormatter())
    plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter())

    gca = plt.gca()
    if format:
        gca.xaxis.set_major_formatter(ticker.FuncFormatter(format_tick))
    gca.yaxis.set_major_formatter(ticker.FuncFormatter(format_tick))

    plt.show()
