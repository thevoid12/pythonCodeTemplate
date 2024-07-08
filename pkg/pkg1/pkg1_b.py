#use black formatter for default formatting
#Use default iterators and operators for types that support them, like lists, dictionaries, and files.
# Yes:  for key in adict: ...
#       if obj in alist: ...
#       for line in afile: ...
#       for k, v in adict.items(): ...


#Always use if foo is None: (or is not None) to check for a None
#Never compare a boolean variable to False using ==. Use if not x: instead. 
#If you need to distinguish False from None then chain the expressions, such as if not x and x is not None:.
#wrong:
a= bool('true')
if a==bool('false'):
  print('hiiii')
#correct:
if not a:
  print('helloo')

#For sequences (strings, lists, tuples), use the fact that empty sequences are false,
# so if seq: and if not seq: are preferable to if len(seq): and if not len(seq): respectively.
testlist=["hello","this","is","test","list"]

if testlist: # this is used instead of if len(testlist)>0
  print("correct")

#intendation is 4 space and maximum 80 words in one line
val=test(a,b, # see how a and c are in same line. if we split code into multiple lines use this format
         c,d)

#Trailing commas in sequences of items are recommended only when the closing container token ], ), or } and 
#does not appear on the same line as the final element. 

#wrong
golomb4 = [
           0,
           1,
           4,
           6,]
#correct
golomb3 = [0, 1, 3] 
golomb4 = [
           0,
           1,
           4,
           6,
           ]
