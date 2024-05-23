#%%
# Import the necessary library and load the datasets
import pandas as pd

# Load Homes for Sale and Real Estate data set
Housing = pd.read_excel("Homes_for_Sale_and_Real_Estate.xlsx")
Housing.head(5)

# %%
# Lets understand Housing data types
Housing.info()

# %%
# Descriptive Analysis
Housing.describe(include='all')

# %%
# Check for blank rows 
blank_rows_housing = Housing[Housing.isnull().any(axis=1)]

# Display the blank rows, if any
if not blank_rows_housing.empty:
    print("Blank rows found in Housing DataFrame:")
    print(blank_rows_housing)
else:
    print("No blank rows found in Housing DataFrame.")


#%%
import re

# Function to extract text from address
def extract_text(address):
    return re.sub(r'\d+', '', address).strip()

# Apply the function to create a new column with only text from 'Address'
Housing['TextAddress'] = Housing['Address'].apply(extract_text)

# Store rows where 'Place' is blank before replacement
blank_rows_before = Housing[Housing['Place'].isnull()]

# Replace blank rows in 'Place' column with text from 'TextAddress' column
Housing['Place'] = Housing['Place'].fillna(Housing['TextAddress'])

# Store rows where 'Place' was replaced
replaced_rows = Housing.loc[blank_rows_before.index]

# Drop the 'TextAddress' column if you don't need it anymore
Housing.drop(columns=['TextAddress'], inplace=True)

# Print replaced rows
print("Replaced Rows:")
print(replaced_rows)

# %%
# Write this to excel
Housing.to_csv("Housing.csv", index=False)

#%%
# Load Community_Points data set
Community = pd.read_csv("Community_Points.csv")
Community.head(5)

#%%
# Lets understand Community Data types
Community.info()

# %%
# Descriptive Analysis
Community.describe(include='all')

#%%
# Check for blank rows 
blank_rows_community = Community[Community.isnull().any(axis=1)]

# Display the blank rows, if any
if not blank_rows_community.empty:
    print("Blank rows found in Housing DataFrame:")
    print(blank_rows_community)
else:
    print("No blank rows found in Housing DataFrame.")

# %%
# I am only using this 2 match the data so I decided not to remove the blank rows
Community.to_csv("Community.csv", index=False)


# %%
