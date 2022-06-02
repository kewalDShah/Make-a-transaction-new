#Initialize a variable to hold your account balance
myBalance=200

#Print the variable displaying your balance
print("Your balance is : ", myBalance)

#Get the receiver's name as input from the user and store it in receiver variable
receiver=input("Enter the receiver name: ")

#Get the amount to transfer as input from the user and store it in amount variable
amount=input("Enter the amount: ")

#Convert the amount value into integer and store it in a variable
amountInInteger=int(amount)


#Add a condition to check if the transfer amount is greater than the available amount in your account and print message accordingly
if (amountInInteger>myBalance):
  print("Insufficient balance")
else:
  #create a dictionary to store transaction details
  transactionData= {"sender":"Kewal", 
                    "receiver":receiver,
                    "Amount":amountInInteger
                    }

  
  #Create a blockData dictionary for storing transaction details 
  blockData = {
    'block': 1,
    'Transaction':transactionData,
  }

  #create a list to store the blockData
  blockTransaction =[]
  
  #Append the block data in the list of blockTransaction
  blockTransaction.append(blockData)
  
  #print all the block transaction details
  print("Transaction details:", blockTransaction)
  
  #Update the account balace after subtracting the transferred amount.
  my_balance=myBalance-amountInInteger
  
  #print the updated account balance.
  print("Your Balance is updated to ",myBalance)  