import nbformat as nbf

notebook_path = r'd:\THE CODE\Python_and_Data_Science\0 ML lecture\32_4.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

# Provided code snippet with a fix for the second scatter plot index
provided_code = """km = KMeans(n_clusters=4, max_iter=100)
y_means = km.fit_predict(X)

plt.figure(figsize=(18, 4))
sns.scatterplot(x=X[y_means==0,0], y=X[y_means==0,1], color='red')
sns.scatterplot(x=X[y_means==1,0], y=X[y_means==1,1], color='green')

plt.tight_layout()
plt.show()"""

# Replace the content of the relevant code cell (the one that previously failed)
# It's at execution_count 8 in the previous view.
modified = False
for cell in nb.cells:
    if cell.cell_type == 'code':
        if "km = KMeans(n_clusters=4" in cell.source:
            cell.source = provided_code
            modified = True
            break

if modified:
    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print("Notebook cell updated with user-provided code.")
else:
    print("Could not find the target cell to update.")
