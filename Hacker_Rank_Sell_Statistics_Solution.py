import sys

# read first integer input variable from STDIN
# In this challenge, this number T is the total number of 'query' and 'sale'
# data lines which will follow as inputs.
T = int(sys.stdin.readline())

#Initialise empty arrays: 1 for the 'sale' type data inputs, and 1 for the
#'query' type data inputs.
Sales_Store = []
Query_Store = []

# The below 'conditions' function will be called for each 'query' type data input line.

# Below this function, the main executing code begins... for Entry in range(T):

# First this splits the parameters in the input line, and assigns first input
# parameter Q or S to variable Type for query or sale type input line.
# if a sale, it parses data appropriately and adds the sale info as an inner array
# inside the Sales_Store array, thus assembling a simple mini-database
# table within this application.

# Otherwise if the data input line is a Query,
# it uses a Python generator expression 'Total' to generate a sum of all the sales which
# are recorded, at this moment in time, in Sales_Store, which satisfy
# the Query conditions.
# Total calls the conditions function on each of the sale inner arrays in the database
# in turn. The function sets and joins 3 condition statements as 'cresult',
# which vary according to data in the Query. If cresult is True, then this sale
# is added to the Total amount, if false it is not.

# This works for 9 of 11 test inputs, not bad I think, but
# it sets the conditions statement separately for each sale record it cycles through in
# Sales_Store. If I can work out how to set conditions statement once, but still cycle
# the different sales records against this one statement, it should reduce
# big O-time to about O(n) and so succeed with largest 2 data input sets.
# I'm finding it tricky with this method because the sale record variable itself is part of cresult conditions
# statement. I expect if ask on Stack Overflow, may find way to solve this.
# eg sal = [1,3,5,4,5]; cond = sal[1] == 1; cond - returns False
# then sal = [1,1,5,4,5]; cond - still returns False.

def conditions(sal, dat, en, pi, ci, si, ri):

    if en == 0:
        cond1 = sal[0] == dat
    else:
        cond1 = (dat <= sal[0] <= en)

    if pi == -1:
        cond2 = True
    elif ci == 0:
        cond2 = (sal[1] == pi)
    else:
        cond2 = (sal[1] == pi and sal[2] == ci)

    if si == -1:
        cond3 = True
    elif ri == 0:
        cond3 = (sal[3] == si)
    else:
        cond3 = (sal[3] == si and sal[4] == ri)

    cresult = cond1 and cond2 and cond3
    return cresult

for ind in range(T):
    Type, d, p, s = [item for item in sys.stdin.readline().strip().split(" ")]

    if "." in d:
        date, end = [int(var) for var in d.split(".")]
    else:
        date = int(d)
        end = 0
    if "." in p:
        p_id, c_id = [int(var) for var in p.split(".")]
    else:
        p_id = int(p)
        c_id = 0
    if "." in s:
        s_id, r_id = [int(var) for var in s.split(".")]
    else:
        s_id = int(s)
        r_id = 0

    if Type == "S":
#        Sales_Store.append({"Date": date, "Product_Id": p_id, "Category_Id": c_id,
#                            "State_Id": s_id, "Region_Id": r_id})
        Sales_Store.append([date, p_id, c_id, s_id, r_id])

    else:
        Total = sum(conditions(sale, date, end, p_id, c_id, s_id, r_id) for sale in Sales_Store)
        Query_Store.append(Total)

for Total in Query_Store:
    print Total
#   or in Python 3: print (Total)