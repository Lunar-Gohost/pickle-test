from ast import Global
import pickle
import os

def Task_Status ():
    # Values
    # First Number - List Number
    # Second Number - Value / Reward
    # Status - 0 Open, 1 In Progress, 2 Closed
    tasklist_filename = 'tasklist1.dat'
    taskList = []
    #pickle
    pickle_out = open("taskList.pickle", "wb")
    pickle.dump(taskList, pickle_out)
    pickle_out.close()
    print("Finished","\n")
    #unpickle
    pickle_in = open("taskList.pickle", "rb")
    taskList = pickle.load(pickle_in)
    print(taskList,"\n")
    task = input("Please select a task ")
    task = int(task)
    print("Selected",taskList[task-1][0],"\n")
    if taskList[task-1][2] == 0:
        status = "Open"
    elif taskList[task-1][2] == 1:
        status = "In Progress"
    elif taskList[task-1][2] == 2:
        status = "Closed"
    print("---------------------")
    print(" Task selected:",taskList[task-1][0],"\n","Reward:",taskList[task-1][1],"\n","Status:",status)
    print("---------------------","\n")
    # taskValue = [0][1]
    # print(taskValue)
    # print("Selected", taskList[0][1])
    # print("Task")
    # -----------------
    # Task:1
    # Reward: 1ETH
    # Status: Open
    # -----------------
def voting (number_of_task, token_wallet_voting):
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


def creat_preposal():#needs to fix pickleing 
    global Perpsoal_creation
    Perpsoal_creation = 'Preposals_creation.dat'

    preposal_creation_list = []

    # first time you run this, "Preposals.dat" won't exist
    #   so we need to check for its existence before we load 
    #   our "database"
    if os.path.exists(Perpsoal_creation):
        # "with" statements are very handy for opening files. 
        with open(Perpsoal_creation,'rb') as rfp: 
            preposal_creation_list = pickle.load(rfp)
        # Notice that there's no "rfp.close()"
        #   ... the "with" clause calls close() automatically! 

    username = input("Please enter your user name:")
    user_preposal = input("Please enter your preposal:")

    new_preposal = username, user_preposal
    preposal_list.append(new_preposal)

    # Now we "sync" our database
    with open(Name_of_Aplacent_list,'wb') as wfp:
        pickle.dump(preposal_list, wfp)

    # Re-load our database
    with open(Name_of_Aplacent_list,'rb') as rfp:
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
global Perpsoal_creation

#Pickle setup(can't be a function)
Name_of_Aplacent_list = 'Preposals12.dat'

preposal_list = []

# first time you run this, "Preposals.dat" won't exist
#   so we need to check for its existence before we load 
#   our "database"
if os.path.exists(Name_of_Aplacent_list):
    # "with" statements are very handy for opening files. 
    with open(Name_of_Aplacent_list,'rb') as rfp: 
        preposal_list = pickle.load(rfp)
    # Notice that there's no "rfp.close()"
    #   ... the "with" clause calls close() automatically! 

# Now we "sync" our database
with open(Name_of_Aplacent_list,'wb') as wfp:
    pickle.dump(preposal_list, wfp)
# Re-load our database
with open(Name_of_Aplacent_list,'rb') as rfp:
    preposal_list = pickle.load(rfp)

print("test",preposal_list)


#add more to the options later
To_do=input("Do you wish to look at preposals, apply for tasks or vote on them? To vote on preposles select vote, to veiw preposlas select veiw, to apply for a preposal selct apply. ")#add ethan's part to the look at


if To_do=="vote":
    vote_on=input("Do you want to vote on, wether a task is done, wether to aprove a aplaction task or somone to do a requested task ")
    #can be used for all voteing 
    if vote_on=="aprove":
        task_perform_filename = 'task_perform.dat'

        Task_perform = []
        if os.path.exists(task_perform_filename):
            with open(task_perform_filename,'rb') as rfp: 
                Task_perform = pickle.load(rfp)
        with open(task_perform_filename,'wb') as wfp:
            pickle.dump(Task_perform, wfp)
        with open(task_perform_filename,'rb') as rfp:
            Task_perform = pickle.load(rfp) 
            print(Task_perform)
        range_needed=item_list_counter(Task_perform)
        for i in range(0,range_needed):
            print("Do you want", Task_perform[i][0], "to perform task", Task_perform[i][1])
            vote_results=voting(range_needed, token_wallet)
            if vote_results=="pass":
                print("user ",Task_perform[i][0], "will do task", Task_perform[i][1])
            if vote_results=="fail":
                print("user ",Task_perform[i][0], "will do not task", Task_perform[i][1])
    #print("Do you wish for, ", user_for_task, "to do task,", task_wish )
    #final_vote=voting ( task_wish, token_wallet)
    #if final_vote=="fail":
    #    print("user ", user_for_task, "cant do task", task_wish)
    #else: 
    #    print ("user ", user_for_task, "will do task", task_wish)   
if To_do=="apply":
    list_length=item_list_counter(Name_of_Aplacent_list)
    aplaction=Task_Aplaction(token_wallet, list_length)  
    print("User", aplaction[0], "wants to perform", aplaction[1])
    task_perform_filename = 'task_perform.dat'

    Task_perform = []

    # first time you run this, "high_task_perform.dat" won't exist
    #   so we need to check for its existence before we load 
    #   our "database"
    if os.path.exists(task_perform_filename):
        # "with" statements are very handy for opening files. 
        with open(task_perform_filename,'rb') as rfp: 
            Task_perform = pickle.load(rfp)
        # Notice that there's no "rfp.close()"
        #   ... the "with" clause calls close() automatically! 

    high_Task_perform = aplaction
    Task_perform.append(high_Task_perform)

    # Now we "sync" our database
    with open(task_perform_filename,'wb') as wfp:
        pickle.dump(Task_perform, wfp)

    # Re-load our database
    with open(task_perform_filename,'rb') as rfp:
        Task_perform = pickle.load(rfp) 
        print(Task_perform)
if To_do=="status":
   statuse=Task_Status ()
   print(statuse)




