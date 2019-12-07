# Making faceted graphs using Seaborn

import seaborn as sns
import matplotlib.pyplot as plt

s = pd.value_counts(data['earliest_cr_line']).to_frame().reset_index()
s.columns = ['date', 'count']

s['year'] = s['date'].dt.year
s['month'] = s['date'].dt.month

d = s[s['year'] > 2008]

plt.rcParams.update(plt.rcParamsDefault)
sns.set_style("whitegrid")

g = sns.FacetGrid(d, col="year")
g = g.map(sns.pointplot, "month", "count")
g.set(xlabel = 'Month', ylabel = '')
axes = plt.gca()
_ = axes.set_ylim([0, d.year.max()])
plt.tight_layout()


# groupby and facet
filtered  = data[data['earliest_cr_line_year'] > 2008]
group = filtered.groupby(['grade', 'earliest_cr_line_year']).agg([np.mean])

graph_df = group['int_rate'].reset_index()

import seaborn as sns
import matplotlib

plt.style.use('fivethirtyeight')
plt.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')

sns.set_style("whitegrid")
g = sns.FacetGrid(graph_df, col="grade", col_wrap = 2)
g = g.map(sns.pointplot, "earliest_cr_line_year", "mean")
g.set(xlabel = 'Year', ylabel = '')
axes = plt.gca()
axes.set_ylim([0, graph_df['mean'].max()])
_ = plt.tight_layout()
