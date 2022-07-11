import pickle
import os
Preposals_filename = 'Preposals2.dat'
preposal_list = []

# first time you run this, "Preposals.dat" won't exist
#   so we need to check for its existence before we load 
#   our "database"
if os.path.exists(Preposals_filename):
    # "with" statements are very handy for opening files. 
    with open(Preposals_filename,'rb') as rfp: 
        preposal_list = pickle.load(rfp)
print (preposal_list)