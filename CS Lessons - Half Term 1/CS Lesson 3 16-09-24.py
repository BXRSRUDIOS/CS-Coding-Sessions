'''
Task 1 
Convert Old Pence, Shillings & Pounds System into New Pounds & Pences System.

12 Pence = 1 Shilling
20 Shillings = 1 Old Pound
240 Pence = 1 Old Pound

Convert everything to pences and then into GBP Pounds
'''



def convert_to_old_system(pounds, pence):
    total_pence = pounds * 100 + pence
    old_pence_in_shilling = 12
    shillings_in_pound = 20
    old_pence_in_pound = 240
    
    old_pounds = total_pence // old_pence_in_pound
    remaining_pence = total_pence % old_pence_in_pound
    old_shillings = remaining_pence // old_pence_in_shilling
    old_pence = remaining_pence % old_pence_in_shilling
    
    return(old_pounds, old_shillings, old_pence)

modern_pounds = 1
modern_pence = 11
old_pounds, old_shillings, old_pence = convert_to_old_system(modern_pounds, modern_pence)
print(f"{modern_pounds}.{modern_pence:02d} GBP is {old_pounds} pounds, {old_shillings} shillings, and {old_pence} pence in the old system.")

def convert_to_modern_system(old_pounds: int, old_shillings: int, old_pence: int):
    old_pence_in_shilling = 12
    shillings_in_pound = 20
    old_pence_in_pound = old_pence_in_shilling * shillings_in_pound
    
    total_old_pence = old_pounds * old_pence_in_pound + old_shillings * old_pence_in_shilling + old_pence
    
    modern_pounds = total_old_pence // 100
    modern_pence = total_old_pence % 100
    
    return modern_pounds, modern_pence


old_pounds = 3
old_shillings = 15
old_pence = 9

modern_pounds, modern_pence = convert_to_modern_system(old_pounds, old_shillings, old_pence)
print(f"{old_pounds} pounds, {old_shillings} shillings, and {old_pence} pence in the old system is {modern_pounds}.{modern_pence:02d} GBP in the modern system.")


    





