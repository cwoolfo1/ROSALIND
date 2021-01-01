print("Enter the DNA string")
input_string = input()
list_one = [x for x in input_string if x == 'A']
list_two = [x for x in input_string if x == 'C']
list_three = [x for x in input_string if x == 'G']
list_four = [x for x in input_string if x == 'T']
one = len(list_one)
two = len(list_two)
three = len(list_three)
four = len(list_four)
print(str(one)+" "+str(two)+" "+str(three)+" "+str(four))