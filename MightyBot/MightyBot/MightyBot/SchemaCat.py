import re                                                # import Regular Expressions
filedir = 'C:\\Python27\\'  # put read file here, or pick a different dir and change filedir
readfilepath = filedir + 'TestyBotMapping_conversions_tests.sql' # copy of readfile included in package, for reference
dbtablelist = []
dbtableset = set()
#set_add = dbtableset.add
with open(readfilepath,'rb') as f2:                      # open file
    for row in f2:                                       # begin for loop
        sqldbtable = ""                                   
        hasfrom   = re.search("FROM ",row)
        hasjoin   = re.search("JOIN ",row)
        hasperiod = re.search(".",row)
        hasspace  = re.search(" ",row)
        hasvt     = re.search("vt_",row)
        if hasfrom:                                      # if row has "FROM ", substring
                sqldbtable = row[row.index('FROM ')+5:]
        elif hasjoin:                                    # if row has "JOIN ", substring
                sqldbtable = row[row.index('JOIN ')+5:]
        else:
            sqldbtable = ""
        if  sqldbtable == "":
            sqldbtable = ""
        else:
            if hasperiod:
                try:
                    sqldbtable = sqldbtable[:sqldbtable.index(' ')]
                except ValueError:
                    sqldbtable = sqldbtable[:sqldbtable.index('.')+40]
            else:
                sqldbtable = ""
        if hasvt:
            sqldbtable = ""
        if sqldbtable != "":
            dbtablelist.append(sqldbtable)
dbtableset = sorted(set(dbtablelist))
for item in dbtableset:
    print item