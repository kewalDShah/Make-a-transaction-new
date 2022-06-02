#Initialize a variable to hold your account balance
my_balance=200

#Initialiize a list to store the block transaction details
blockTransaction =[]

#Print the variable displaying your balance
print("Your balance is : ", my_balance)

#Initialize a variable to take input from user about receiver's name
receiver=input("Enter the receiver name: ")

#Initialize a variable to take input from user about amount to transfer
amount=input("Enter the amount: ")

#Convert the input of amount from string to int
amount=int(amount)


#Add a condition to check if the transfer amount is greater than the amount of available in your account
if (amount>my_balance):
  
  #print a message that the amount is insufficient to transfer
  print("Insufficient Code")
  
#add a else conditon
else:
  
  #Intialize a dictionary for storing transaction details
  transactionData= {"sender":"Kewal", 
                    "receiver":receiver,
                    "Amount":amount
                    }

  
  #Initialize a dictionary to store the block data 
  blockData = {
  
    #create a key-value pair for sotring block count
    'block': 1,
    
    #create a key-value pair for stroing the transaction data
    'Transaction':transactionData,
  }
  
  #Append the block data in the list of blockTransaction
  blockTransaction.append(blockData)
  
  #print the list comprising block transaction details
  print("Transaction details:", blockTransaction)
  
  #Subtract the amount transferred from your available balance.
  my_balance=my_balance-amount
  
  #print the variable with the updated account balance.
  print("Your Balance is updated to ",my_balance)  