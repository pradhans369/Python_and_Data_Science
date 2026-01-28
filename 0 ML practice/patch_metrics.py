
import json

def patch_notebook():
    file_path = r'd:\THE CODE\Python_and_Data_Science\0 ML practice\11 gradient descent.ipynb'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = cell['source']
            new_source = []
            changed = False
            for line in source:
                if 'print(f"ACCURACY SCORE : {accuracy_score(y_test, y_pred)}")' in line:
                    new_source.append('print(f"R2 SCORE : {r2_score(y_test, y_pred)}")\n')
                    new_source.append('print(f"MAE : {mean_absolute_error(y_test, y_pred)}")\n')
                    new_source.append('print(f"MSE : {mean_squared_error(y_test, y_pred)}")\n')
                    changed = True
                else:
                    new_source.append(line)
            if changed:
                cell['source'] = new_source

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)

if __name__ == "__main__":
    patch_notebook()
    print("Notebook patched successfully.")
