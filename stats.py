def get_book_text(file_path):
    with open(file_path) as f:
        file=(f.read())
        return file

def get_num_words():
   counter=0
   file=get_book_text('/Users/ago/workspace/github.com/bootdev/bookbot/books/frankenstein.txt')
   split_file=file.split()
   for words in split_file:
       counter+=1
   print(f'{counter} words found in the document')           
   

def count_characters(file):
    dic={}
    
    file_lower=file.lower()
    #print(file_lower)
    for words in file_lower:
        dic[words]=0
    for letters in file_lower:
        if letters in dic:
            dic[letters]+=1
    return dic


def listed(dict):
    list=[]
    for items in dict:
        list.append({'character':items, 'count':dict[items]})
    return list

def sort_on(dict):
    return dict['count']

