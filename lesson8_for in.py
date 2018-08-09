#for in

rabbits= ['black','white','gray','brown'];
current=0;
while current< len(rabbits):
    print(rabbits[current]);
    current+=1;

for rabbit in rabbits:
    print(rabbit); # a better version to select the items in the list
    
word='cat';
for letter in word:
    print(letter);

accusation={'room':'ballroom',
            'weapon':'pipe',
            'person':'col. Mustard'
            };
for key in accusation:
    print(key);
for value in accusation.values():
    print(value);
for item in accusation.items():
    print(item);
for key, contents in accusation.items():
    print(key, 'has the content', contents);
    
    


    
    