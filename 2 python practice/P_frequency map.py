# storing frequency of numbers into a dictionary

nums_list = [1,1,3,35,46,5,3,1,454,93,3,33,5,5,3,3,6,5,3,46,3,1,3,126,36,5]


def frequency(list):
    num_dict={}
    for i in list:
        if i not in num_dict:
            num_dict[i]=1
        else:
            num_dict[i]+=1
    
    return num_dict

print(frequency(nums_list))

a = frequency(nums_list)

# ----------------------------------------------------------------------------------------------------------------
print()
print(a.keys())
print()
print(a.values())






