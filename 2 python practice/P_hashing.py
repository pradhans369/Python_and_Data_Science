
hash_table_size = 10
hash_table = [None] * hash_table_size

print(hash_table)
print("--------------------------------------------------------------")

# def hash_function(key):
    # return key % hash_table_size

def insert(index, value):
    hash_table[index] = value
    print(f"INSERTED {value} AT INDEX {index}")


# -----------------------------------------------------------------

print("--- Inserting Data ---")
insert(4, "Alice")   # 104 % 10 = 4
insert(7, "Bob")     # 207 % 10 = 7
insert(2, "Charlie") # 902 % 10 = 2

print("\n--- Hash Table State ---")
print(hash_table)
print(hash_table[2])
print(hash_table[4])
print("--------------------------------------------------------------")

nums_list = [1,1,3,35,46,5,3,1,454,93,3,33,5,5,3,3,6,5,3,46,3,1,3,126,36,5]
hash_list = [None] * 20

def hash(list):    # will take nums_list
    for i in list:
        index = i % len(hash_list)
        start_index = index
        
        while hash_list[index] is not None a






