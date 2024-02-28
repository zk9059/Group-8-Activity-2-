

'''

Activity 2 done by  khaled abusharbain ,, zarak khan,, nour abdelwahed

contribution: 
zarak : Conversion_direction_selection function, dollar_to_aed(amount), def menu, amount to be converted function

khaled: Other_currencies_to_Aed , aed_to_eur(money), aed_to_britishPound(money) , def main, aed to other currency

nour:  def britishPound_to_aed(amount): def eur_to_aed(amount):

khaled repo: https://github.com/KhaledAmer1/Khaled-Abusharbain2651
zarak repo :     https://github.com/zk9059/Group-8-Activity-2
Nour Abdelwahed : https://github.com/NourAbdElWahe/Group-8-Activity-2



'''






#listed here are all the conversion rates in variables


Aed_to_Eruo=0.25
Aed_to_British_pound= 0.22
Aed_to_Dollars= 0.27
Dollar_to_AED= 3.67
British_Pound_to_Aed= 4.65
Euro_to_AED= 3.98

def Menu():  ## starting menu
    print("          Main Menu  ")
    print("welcome to the Currency Converter ")
    print('------------------------------------')
    print("")


def Conversion_direction_selection():
    
    print("select one of the following options:")
    selection=int(input("Select the conversion direction: \n 1. AED to other currencies \n 2. Other currencies to AED \n 3. Exit \n"))
    if selection ==1: ## if user chooses 1  it directts to 
        print("decision 1 ") 
        Money= Amount_to_be_Converted() # value for money
        
        AED_to_other_currencies(Money)

    elif selection== 2: # if user chooses 2 it directs to 
        print("decision 2")  
        Amount = Amount_to_be_Converted()
        Other_currencies_to_Aed(Amount)

    else:  # if not 1 or 2 just exit program
        print('exiting program' )
        exit()    


#THIS IS FOR OTHER CURRENCIES TO AED


def Other_currencies_to_Aed(Amount):

    print('enter choices 1/ 2 or 3')
    print('1. Euro (EUR) to AED')
    print('2. British Pound (GBP) to AED')
    print('3. Dollar to AED')
    print('4. Exit')
    Choice_Currency = int(input('enter subchoice here '))
    if Choice_Currency ==1 : ## if user chooses 1 which is equal to euro to aed 
        eur_to_aed(Amount)
    elif Choice_Currency == 2: # if user chooses 2 which is equal to britch pound to aed
        britishPound_to_aed(Amount)
    elif Choice_Currency==3: # if user chooses 3 which is equal to dollar to aed
        dollar_to_aed(Amount)
    else:
        exit()         # if user doesnt chooses just exit


def dollar_to_aed(Amount): # process of converting dollar to aed
    Converted_Result= Amount * Dollar_to_AED
    print('the amount in aed is ' + str(Converted_Result))


def britishPound_to_aed(Amount): # process of converting britch to aed
    Converted_Result= Amount*British_Pound_to_Aed
    print('the amount in AED is '+ str(Converted_Result))


def eur_to_aed(Amount): # process of converting euro to aed
    Converted_Result= Amount*Euro_to_AED
    print(Amount +' in AED is '+ Converted_Result )

def Amount_to_be_Converted(): ## user input amount that is going to be convertied
    print("input the amount of money you would like to convert")
    Amount= float(input(""))
    return Amount

#the following code is for AED to other currencies 
        

def AED_to_other_currencies(Money ): # from aed to other currencies
   

    #decide which currecny you want to take 
    print('money ')
    print("Enter Choice 1/2/3 ")
    print("1. AED to Euro (EUR)")
    print('2. AED to British Pound (GBP)')
    print("3. AED to US Dollar")
    print("4. AED to Exit")
    Which_currency=int(input('')) # users choice of which currency they require

    if Which_currency ==1: # if user chooses 1 it directs to aed to eur
        aed_to_eur(Money)
    elif Which_currency == 2:
        aed_to_britishPound(Money)
    elif Which_currency ==3:
        aed_to_dollar(Money)    
    else:
        exit()    

def aed_to_britishPound(Money): # process of converting aed to britch
    Converted_result= Money*Aed_to_British_pound
    print(str(Money)+' in British Pounds'+ str(Converted_result))

def aed_to_eur(Money):
    print(Money)
    Converted_Result=Money * Aed_to_Eruo # process of converting aed to eur
    print(str(Money)+'in Euros is '+ str(Converted_Result))

def aed_to_dollar(Money):
    print("Aed to dollar")    
    Converted_Result= Money*Aed_to_Dollars
    print(str(Money)+" in dollars is "+ str(Converted_Result))

def main():
    Menu()

    Conversion_direction_selection()
    

main()
