import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.colors as mcolors


def format_tick(value, _):
    return '{:,.0f}'.format(value)


def run_chart():
    hex_colors = ["#FFDDDD", "#FFCCCC", "#FFBBBB", "#FFAAAA", "#FF9999", "#FF8888", "#FF7777", "#FF6666", "#FF5555",
                  "#FF4444",
                  "#FF3333", "#FF2222", "#FF1111", "#FF0000", "#FF0000", "#EE0000", "#DD0000", "#CC0000", "#BB0000",
                  "#AA0000"]

    df = pd.read_csv('data.csv')
    df = df.dropna()

    title_x = "VDAE (venitul disponibil pentru achitarea energiei)"
    title_y = "CERPA (costul energiei in perioada rece a anului)"

    max_x = 100000
    max_y = 20000

    df['VDAE'] = df['VGL'] - df['MCF'] - df['RLCI']
    df['R'] = (df['CERPA']/df['VDAE']) * 100

    sns.set_style('whitegrid')

    for i in range(20):
        x = (i+1)*5
        df2 = df[df['R'] <= x]
        df2 = df2[df2['R'] > x-5]
        sns.scatterplot(data=df2, x='VDAE', y='CERPA', color=hex_colors[i], edgecolor='black')
    sns.scatterplot(data=df[df['R'] > 100], x='VDAE', y='CERPA', color='black', edgecolor='black')



    plt.title("Raportul dintre cheltuielile pentru resursele energetice si venitul disponibil pentru achitarea energiei")
    plt.ylabel(title_y)
    plt.xlabel(title_x)

    plt.xlim(0, max_x+500)
    plt.ylim(0, max_y+500)

    gca = plt.gca()

    legend_labels = ['{}-{}'.format(i, i+5) for i in range(5, 100, 5)]
    legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=hex_color, markersize=10, markeredgecolor='black') for
                      hex_color in hex_colors]
    gca.legend(legend_handles, legend_labels, loc='right', bbox_to_anchor=(1.125, 0.5))

    if format:
        gca.xaxis.set_major_formatter(ticker.FuncFormatter(format_tick))
    gca.yaxis.set_major_formatter(ticker.FuncFormatter(format_tick))

    plt.show()
