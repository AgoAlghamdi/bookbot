from stats import *
import sys

if len(sys.argv)<2:
    sys.exit('Usage: python3 main.py <path_to_book>')

file=get_book_text(sys.argv[1])
dic=count_characters(file)

listed_dic=listed(dic)
total=0

listed_dic.sort(reverse=True,key=sort_on)

print('============ BOOKBOT ============')
print('Analyzing book found at books/frankenstein.txt...')
print('----------- Word Count ----------')
for items in listed_dic:
    alpha=items['character']
    if alpha.isalpha()==True:
        total+=items['count']
print(f'Found {total} total words')

print('--------- Character Count -------')    
for items in listed_dic:
    alphabet=items['character']
    if alphabet.isalpha()== True:
        print(f'{items['character']}: {items['count']}')





    #print(items)
    
#print(listed_dic)