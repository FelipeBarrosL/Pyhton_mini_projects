
pi = 3.14

def vol(rad):
    return (4*pi*(rad**3)/3)

print(vol(2))

def ran_check(num, low, high):
    if num <= high and num >= low:
        print(f"Number {num} is between {low} and {high}.")
    else:
        print("HI")
        pass

ran_check(5, 2, 7)

def up_case(sample_string):
    upper = 0
    for i in range(len(sample_string)):
        if sample_string[i].isupper() == True:
            upper += 1
    print(f"Number of uppers: {upper} Number of lowers: {len(sample_string)-upper} ")

up_case("New FILes Is 8")

def unique_list(list):
    stored = []
    for i in list:
        if list[i] in stored:
            continue  
        else:
            stored.append(list[i])     
    print(stored) 

numbers = [1,1,1,2,3,4,5,5,5,5,5,]
unique_list(numbers)

