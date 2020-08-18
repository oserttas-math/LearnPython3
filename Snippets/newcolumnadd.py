# If your data conversion involves just one column, simply use the map() function on the column (in essence, it’s a Series object).
# If your data conversion involves multiple columns, use the apply() function.

# Create a new column using the map() function
df_wide['before_meds_unit'] = df_wide['before_meds'].map(lambda x: f"{x} ng/ml")

# Create a new column using the apply() function
df_wide['change_meds'] = df_wide.apply(
    lambda x: x['after_meds'] - float(x['before_meds_unit'].split()[0]),
     axis=1
)
