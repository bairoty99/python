#-----------------------------
#----  For Nested Loop  ------
#-----------------------------

languages={
    "mohanad":{
        "rating":"Bad",
        "progress":"10%"
        },
    "ali":{
        "rating":"Good",
        "progress":"70%"
    },
    "Bairoty":{
        "rating":"very Good",
        "progress":"100%"
    }
    
}
# print(languages.items())# [(key,value),(key,value)]
for name_keys,name_value in languages.items():
    print(f"Information Of This user=>[ {name_keys} ] Is:")
    for info_keys,info_value in name_value.items():
        print(f" - {info_keys.capitalize()} Is {info_value}")