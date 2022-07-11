import pickle
import os



Preposals_filename = 'Preposals12.dat'

preposal_list = []

# first time you run this, "Preposals.dat" won't exist
#   so we need to check for its existence before we load 
#   our "database"
if os.path.exists(Preposals_filename):
    # "with" statements are very handy for opening files. 
    with open(Preposals_filename,'rb') as rfp: 
        preposal_list = pickle.load(rfp)
    # Notice that there's no "rfp.close()"
    #   ... the "with" clause calls close() automatically! 

# Now we "sync" our database
with open(Preposals_filename,'wb') as wfp:
    pickle.dump(preposal_list, wfp)
# Re-load our database
with open(Preposals_filename,'rb') as rfp:
    preposal_list = pickle.load(rfp)

print(preposal_list)