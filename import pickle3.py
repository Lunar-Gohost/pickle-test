from ast import Global
import pickle
import os
import re


def voting ( number_of_task, token_wallet_voting):
    postive_vote=0
    negitve_vote=0
    vote_test1="fail"
    if token_wallet_voting<=0:
        print("you cant vote")
        return
    if token_wallet_voting>=1:
        while vote_test1=="fail":
            vote_choice=input("do you wish for this action to pass, [y/n] "  )
            if vote_choice=="y" or vote_choice=="n":
                vote_test1="pass"
            else:
                print("please input y or n")

        if vote_choice=="y":
            postive_vote=postive_vote+token_wallet_voting
        else:
            negitve_vote=negitve_vote+token_wallet_voting
        if postive_vote>negitve_vote:
            Vote_statuse="pass"
            
        else:
            Vote_statuse="fail"
        return(Vote_statuse)


def creat_preposal():
    Preposals_filename = 'Preposals2.dat'

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

    username = input("Please enter your user name:")
    user_preposal = input("Please enter your preposal:")

    new_preposal = username, user_preposal
    preposal_list.append(new_preposal)

    # Now we "sync" our database
    with open(Preposals_filename,'wb') as wfp:
        pickle.dump(preposal_list, wfp)

    # Re-load our database
    with open(Preposals_filename,'rb') as rfp:
        preposal_list = pickle.load(rfp)

    print(preposal_list)
    return


def Task_Aplaction(token_wallet_ta, last_number_ta):  
    if token_wallet_ta<=0:
        print("You cant perform a task without a roast beef token")
        return()
    if token_wallet_ta>=1:
        test3="fail"
        while test3=="fail": 
            task_wish=input("Put in the number of the task you are applying for ")
            if str.isnumeric(task_wish):
                task_wish=int(task_wish)
                if task_wish>=1 and task_wish<=last_number_ta:
                    test3="pass"
                else:
                    print("put in an int.(number) and make sure its a valid task")
            else:
                print("put in an int.(number) and make sure its a valid task")

    user_for_task=input("Your name, ")
    user_request=(user_for_task, task_wish)
    return(user_request)


def item_list_counter(list_ilc):
    list_count=list(list_ilc)
   
    for i in range(0, len(list_count)):
  
        if i == (len(list_count)-1):
            last_number=i+1
            return(last_number)
#-------------------------------------------------------------------------------------------
#varbals
token_wallet=1
curent_status_main="available"    
global preposal_list

#Pickle setup(can't be a function)
Preposals_filename = 'Preposals2.dat'
preposal_list = "high_scores.dat"

# first time you run this, "Preposals.dat" won't exist
#   so we need to check for its existence before we load 
#   our "database"
if os.path.exists(Preposals_filename):
    # "with" statements are very handy for opening files. 
    with open(Preposals_filename,'rb') as rfp: 
        preposal_list = pickle.load(rfp)
print (preposal_list)

#add more to the options later
To_do=input("Do you wish to look at preposals, apply for tasks or vote on them? To vote on preposles select vote, to veiw preposlas select veiw, to apply for a preposal selct apply. ")#add ethan's part to the look at
if To_do=="vote":
    
    print("Do you wish for, ", user_for_task, "to do task,", task_wish )
    final_vote=voting ( task_wish, token_wallet)
    if final_vote=="fail":
        print("user ", user_for_task, "cant do task", task_wish)
    else: 
        print ("user ", user_for_task, "will do task", task_wish)   
if To_do=="apply":
    list_length=item_list_counter(preposal_list)
    aplaction=Task_Aplaction(token_wallet, list_length)  
    print("User", aplaction[0], "wants to perform", aplaction[1])




