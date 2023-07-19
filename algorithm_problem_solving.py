"""Algorithm Problem Solving """
import re

def convert_getter_to_field_name(getter_name):
    # Remove the 'get' prefix
    field_name = getter_name[3:]
    
    # Split the field name by capital letters
    field_name_parts = re.findall('[A-Z][a-z]*', field_name)
    
    # Join the field name parts with underscores
    converted_name = '_'.join(field_name_parts)
    
    # Convert the name to lowercase
    converted_name = converted_name.lower()
    
    return converted_name
 
getter_name = 'getLongAccountName'
field_name = convert_getter_to_field_name(getter_name)
print(field_name)  # Output: long_account_name