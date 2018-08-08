#!usr/bin/pythion3.5
#join

marxes=['groucho','chico','harpo'];
print(marxes);
joinString= ', '.join(marxes);
print(joinString);
marxess=joinString.split(', ');
print(marxess);

#sort() sort a list itself
#sorted() copy a sorted list

marxes=['groucho','chico','harpo'];
sorted_marxes= sorted(marxes);
print(sorted_marxes);

print('marxes:',marxes)

marxes.sort();
print("marxes after sort:",marxes)

numbers=[1,2,4.0,3]
print(numbers);
numbers.sort();
print('numbers after sort',numbers)
numbers.sort(reverse=True);
print('reverse number',numbers)


