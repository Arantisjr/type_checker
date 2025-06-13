from decorator import type_checker

@type_checker
def name_age(name: str, age: int) -> str: print(f"Name: {name} & Age: {age}"); return True
name_age(age=15, name='4')

