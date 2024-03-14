import collections


# this gives the rightmost numbers of the pyramid number sequences which
# we only need
def generate_sequence(n):
    rightmost_nums = []
    list=[0]
    for i in range(1,n+1):
        num = list[i-1]+i
        rightmost_nums.append(num)
        list.append(num)
    return rightmost_nums


#converting the given file to a dictionary so that it is easy to process later
def file_to_dict(filename):
    with open(filename) as decode:
        content = decode.read()
        newstring_list = content.split('\n')

        text_dict = {element.split(' ')[0]: element.split(' ')[1] for element in newstring_list if len(element.split(' '))==2}
        # print(text_dict)
        # same as above but with for loop
        # text_dict = {}
        # for elmnt in newstr:
        #     t = elmnt.split(' ')
        #     if(len(t)==2):
        #         text_dict[t[0]]=t[1]
        # print(text_dict)
        return text_dict

# Get the highest number which we got from the text file so that
# we can generate the sequence up to that number
def max_number(dict):
    max_num = 0
    for key in dict:
        k = int(key)
        if k >=max_num:
            max_num=k

    return max_num

# here we decode using our functions and then return it
def decode(filename):
    dict_from_file = file_to_dict(filename)
    max_num = max_number(dict_from_file)
    sequence = generate_sequence(max_num)
    final_output = ""
    for i in sequence:
        if(str(i) in dict_from_file):
            final_output += f"{dict_from_file[str(i)]} "
    return final_output

decoded_words = decode("coding_qual_input.txt")
print(decoded_words)
