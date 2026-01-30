import nbformat
import numpy as np

notebook_path = r'd:\THE CODE\Python_and_Data_Science\0 ML practice\11 gradient descent.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# 1. Modify the feature selection and engineering cell (Cell 7)
# Original Cell 7 content:
# df2 = df[['month', 'city_0', 'city_1', 'city_2', 'city_3', 'city_4', 'city_5', 'sqft_living', 'sqft_lot', 'waterfront', 'view', 'price']]
# # since year and country are both constant feature adding no value, hence we have to remove them 
# df2.head()

new_cell_source = """# Handling outliers and feature refinement
df2 = df.copy()

# 1. Apply log transformation to the target variable 'price'
# This helps normalize the skewed distribution.
df2['price_log'] = np.log1p(df2['price'])

# 2. Apply log transformation to skewed features
df2['sqft_living_log'] = np.log1p(df2['sqft_living'])
df2['sqft_lot_log'] = np.log1p(df2['sqft_lot'])

# 3. Capping (Winsorization) at 99th percentile to handle remaining extreme outliers
upper_living = df2['sqft_living_log'].quantile(0.99)
df2['sqft_living_log'] = np.where(df2['sqft_living_log'] > upper_living, upper_living, df2['sqft_living_log'])

upper_lot = df2['sqft_lot_log'].quantile(0.99)
df2['sqft_lot_log'] = np.where(df2['sqft_lot_log'] > upper_lot, upper_lot, df2['sqft_lot_log'])

# 4. Correct categorical encoding for 'statezip'
# Instead of numerical, treat it as categorical using BinaryEncoder
encoder_zip = ce.BinaryEncoder(cols=['statezip'])
df2 = encoder_zip.fit_transform(df2)

# 5. Final feature selection
# Drop original columns that were log-transformed and redundant square footage columns
# Keep 'waterfront' and 'view' as they are important for price
features_to_drop = ['price', 'date', 'street', 'city', 'country', 'year', 'sqft_living', 'sqft_lot', 'sqft_above', 'sqft_basement']
df2 = df2.drop(columns=features_to_drop, errors='ignore')

print("New Feature Set:", df2.columns.tolist())
df2.head()"""

# Find and replace Cell 7
nb.cells[7].source = new_cell_source

# 2. Modify first training cell (Cell 9) to use new target and features
new_train_cell_9 = """X = df2.drop(columns=['price_log'])
y = df2['price_log']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_log = lr.predict(X_test)

# Convert back from log scale for evaluation in actual dollars
y_test_actual = np.expm1(y_test)
y_pred_actual = np.expm1(y_pred_log)

print(f"R2 SCORE (Log-Price): {r2_score(y_test, y_pred_log)}")
print(f"MAE (Actual Dollars): {mean_absolute_error(y_test_actual, y_pred_actual)}")
print(f"R2 SCORE (Actual Dollars): {r2_score(y_test_actual, y_pred_actual)}")"""

nb.cells[9].source = new_train_cell_9

# 3. Modify second training cell (Cell 10) for scaled features
new_train_cell_10 = """X = df2.drop(columns=['price_log'])
y = df2['price_log']

std = StandardScaler()
X_scaled = std.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_log = lr.predict(X_test)

y_test_actual = np.expm1(y_test)
y_pred_actual = np.expm1(y_pred_log)

print(f"R2 SCORE (Scaled, Log-Price): {r2_score(y_test, y_pred_log)}")
print(f"MAE (Actual Dollars): {mean_absolute_error(y_test_actual, y_pred_actual)}")
print(f"R2 SCORE (Actual Dollars): {r2_score(y_test_actual, y_pred_actual)}")

# Let's see the feature importance (coefficients)
coeffs = pd.Series(lr.coef_, index=X.columns).sort_values(ascending=False)
print("\\nTop Feature Influencers:")
print(coeffs.head())"""

nb.cells[10].source = new_train_cell_10

with open(notebook_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print("Notebook patched successfully.")
