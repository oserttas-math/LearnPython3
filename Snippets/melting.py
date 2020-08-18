# if the table created in a wide format
df = pd.DataFrame({'subject': [100, 101, 102],
                         'before_meds': [5.5, 7.7, 6.6],
                         'after_meds': [4.4, 5.8, 4.9]})
                         
                         
                         
# convert the table to long format
df_wide = df.melt(id_vars='subject', value_vars=['before_meds', 'after_meds'],
           var_name=['time_point'], value_name='measure')
           
           
# Long format to Wide format
df_long = df_wide.pivot(index='subject',
                        columns='time_point',
                        values='measure')

