#create empty

empty_dict={};
print(empty_dict);

bierce={
    'day':'A period of 24 hrs.',
    'week':'A period of 7 days.',
    'month':'A period of 4 weeks.'
    }
print(bierce);

#dict()

lol=['a','b',],['c','d'],['e','f'];
print(dict(lol));

#key()

pythons={'mom':'Mary',
         'dad':'Tode',
         'sister':'Josephina',
         'brother':'Ginter',
         'pet':'Lulu'
         }
print(pythons);

#add

pythons['neighbor']='Bronx'
print(pythons);
pythons['neighbor']='Holland'
print(pythons);

#with updat()

pythons={'mom':'Mary',
         'dad':'Tode',
         'sister':'Josephina',
         'brother':'Ginter',
         'pet':'Lulu',
         'neighbor':'Holland'
         }
others={'teacher':'Shirley',
        'classmate':'Trippie Redd'
        }
pythons.update(others);
print(pythons);

first={'a':1,'b':2}
second={'b':'poop'}
first.update(second);
print(first);
       
#del

del pythons['teacher'];
print(pythons);

#clear(),{}

pythons.clear();
print(pythons);
pythons={};
print(pythons);

pythons={'mom':'Mary',
         'dad':'Tode',
         'sister':'Josephina',
         'brother':'Ginter',
         'pet':'Lulu',
         'neighbor':'Holland',
         }

#in

print('mom' in pythons);
print('pet' in pythons);
print('teacher' in pythons);

#[key]

print(pythons['dad']);
if 'classmate' in pythons:
    print(pythons['classmate']);
else: 
    print('none');

#dictionary get()
    
print(pythons.get('mom'));
print(pythons.get('brother'));
print(pythons.get('teacher'));
print(pythons.get('teacher','not a member'));

signals={'green':'go',
         'yellow':'go faster',
         'red':'stop',
         }
#keys
print(list(signals.keys()));
#values
print(list(signals.values()));
#items
print(list(signals.items()));

original_signals=signals.copy();

      
    
