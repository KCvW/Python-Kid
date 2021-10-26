# Creating a dictionary
acronyms = {'LOL' : 'laugh out loud' ,
            'IDK' : "I dont't know" ,
            'THB' : 'to be honest'}

# Writing a sentence
sentence = 'IDK' + ' what happend ' + 'THB'
translation = acronyms.get('IDK') +' what happend ' + acronyms.get('THB')

# Printing the sentence
print('sentence:', sentence)
print('translation', translation)