import matplotlib, sys
matplotlib.use('Agg')
import matplotlib.pyplot as m_plot


if __name__=='__main__':
    counts = []
    dates = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            day, value = line.strip().split('\t')
            counts.append(int(day))
            dates.append(int(value))
    fig = m_plot.figure(figsize=(7, 8))
    fig.suptitle('Trips vs Time', fontsize=20)
    Ax = fig.add_subplot(111)
    Ax.plot(counts, dates, 'o')
    fig.savefig(sys.argv[2])
