# To find out the number of duplicates
df.duplicated().sum()
df.duplicated(keep=False).sum()



# Get the duplicate records
duplicated_indices = df.duplicated(['col0', 'col1'], keep=False)
duplicates = df.loc[duplicated_indices, :].sort_values(by=['col0', 'col1'], ignore_index=True)

# Drop the duplicate records
df.drop_duplicates(['col0', 'col1'], keep="first", inplace=True, ignore_index=True)
