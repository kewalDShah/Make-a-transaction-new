#Initialize a variable to hold your account balance
myBalance=200

#Print the variable displaying your balance
print("Your balance is : ", myBalance)

#Initialize a variable to take input from user about receiver's name
receiver=input("Enter the receiver name: ")

#Initialize a variable to take input from user about the amount to be transferred
amount=input("Enter the amount: ")

#Convert the input of amount from string to int
amount=int(amount)


#Add a condition to check if the transfer amount is greater than the available amount in your account and print message accordingly
if (amount>myBalance):
  print("Insufficient Code")
else:
  #Intialize a dictionary for storing transaction details
  transactionData= {"sender":"Kewal", 
                    "receiver":receiver,
                    "Amount":amount
                    }

  
  #Initialize a dictionary to store the block data 
  blockData = {
    'block': 1,
    'Transaction':transactionData,
  }

  #Initialize a list to store the blocks  
  blockTransaction =[]
  
  #Append the block data in the list of blockTransaction
  blockTransaction.append(blockData)
  
  #print the al comprising block transaction details
  print("Transaction details:", blockTransaction)
  
  #Update the account balace after subtracting the transferred amount.
  my_balance=myBalance-amount
  
  #print the variable with the updated account balance.
  print("Your Balance is updated to ",myBalance)  