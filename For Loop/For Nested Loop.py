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

for name in languages:
    print(f"Information Of This user {name} Is:")
    for info in languages[name]:
        print(f" - {info.capitalize()} Is {languages[name][info]}")