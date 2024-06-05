import copy
munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}
demo = copy.deepcopy(munsters)
def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"


print(mess_with_demographics(demo))
print(munsters)

'''yes, mess_with_demographic does alter munsters bc
dicts are mutable so as he loops through it in mess_with_demographics
it alters the original munsters
it goes through each persons age and gender and alters it
they all have other as their gender and 42 added to their real age'''
