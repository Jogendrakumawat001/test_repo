'''
a. Display all employees' names for the given project manager name.
b. Display name of only those employees’ whose experience is more than 4 years.
c. Update years of experience with 4.6 whose experience is greater than 3.5 and
less than 4.5 year.
d. Display TL with their year of experience, if has no experience 
then display N/A.
e. Smith left the company and all his members were assigned to Ryan.
f. Check company has any employee who has less than 2 years of experience.
g. Check Edge is TL or not if not make him TL.
'''
company = {
    "Robert": {
        "mark": {
            "experience": 8,
            "POST": "TL",
            "memb": {
                "Leonardo": {
                    "experience": 1
                },
                "Alexander": {
                    "experience": 1
                }
            }

        },
        "smaual": {
            "experience": 8,
            "POST": "TL"

        },
        "paul": {
            "experience": 8,
            "POST": "TL",
            "memb": {
                "Feogl": {
                    "experience": 4.5
                }
            }
        },
        "Tom": {
            "experience": 8,
            "POST": "TL",
            "memb": {
                "jerry": {
                    "experience": 1.5
                },
                "john": {
                    "experience": 1.6
                }
            }
        }
    },
    "Anne": {
        "chriss": {
            "experience": 5,
            "POST": "TL",
            "memb": {
                "James": {
                    "POST": "TL",
                    "experience": 0,
                    "memb": {
                        "jennifer": {
                            "experience": 3.8
                        },
                        "scott": {
                            "experience": 3.8
                        },
                        "sophie": {
                            "experience": 3.8
                        }
                    }
                }
            }
        },
        "pratt": {
            "experience": 5,
            "POST": "TL"
        },
        "emma": {
            "experience": 5,
            "POST": "TL"
        },
        "will": {
            "experience": 5,
            "POST": "TL",
            "memb": {
                "Edge": {
                    "experience": 3,
                    "POST": "SD"
                },
                "Ryan": {
                    "experience": 3.5,
                    "POST": "SD"
                }
            }
        },
        "smith": {
            "experience": 5,
            "POST": "TL",
            "memb": {
                "Walker": {
                    "experience": 2.7
                },
                "Diana": {
                    "experience": 2.7
                }
            }
        }
    }
}


# Step A


def all_employee(n):
    '''Display all employees' names for the given project manager name.'''
    all_emp = []
    d = company.get(n)
    for i in d.keys():
        all_emp.append(i)
        k = company[n][i]
        if "memb" in k.keys():
            for j in k["memb"].keys():
                all_emp.append(j)
                if "memb" in k["memb"][j].keys():
                    for l in k["memb"][j]["memb"].keys():
                        all_emp.append(l)
    return all_emp


# Step B
def exp_more_than_4():
    '''Display name of only those employees’ whose experience is more than 4 years.'''
    l = []
    for manager, team in company.items():
        for employee, details in team.items():
            if "memb" in details:
                for member, member_details in details["memb"].items():
                    if member_details["experience"] > 4:
                        l.append(member)
            else:
                if details["experience"] > 4:
                    l.append(employee)
    return l


# Step C

def update_experience(members):
    '''Update years of experience with 4.6 whose experience is greater than 3.5 an less than 4.5 year.'''
    for j in members.keys():
        e = members[j].get("experience")
        if e and 3.5 < e < 4.5:
            members[j]["experience"] = 4.6
        if "memb" in members[j].keys():
            update_experience(members[j]["memb"])


def change_exp():
    for team in company.values():
        for role in team.values():
            if "memb" in role.keys():
                update_experience(role["memb"])


# strp D


def tl_exp():
    '''Display TL with their year of experience, if has no experience then display N/A'''
    tl_dict = {}
    for i in company.keys():
        for j in company[i].keys():
            exp = company[i][j]["experience"]
            tl_dict[j] = exp
            if "memb" in company[i][j].keys():
                for k in company[i][j]["memb"]:
                    for l in company[i][j]["memb"][k].keys():
                        if company[i][j]["memb"][k][l] == "tl_dict":
                            exp = company[i][j]["memb"][k]["experience"]
                            tl_dict[k] = exp
    return tl_dict


# Step E


def smith_remove():
    '''Smith left the company and all his members were assigned to Ryan.'''
    d = company.get("Anne")
    smith_memb = d.get("smith").get("memb")
    d.get("will").get("memb").update(smith_memb)
    del d["smith"]


# Step F
def check_experience():
    '''Check company has any employee who has less than 2 years of experience'''
    l = []
    for manager, team in company.items():
        for employee, details in team.items():
            if "memb" in details:
                for member, member_details in details["memb"].items():
                    if member_details["experience"] < 2:
                        l.append(member)
            else:
                if details["experience"] < 2:
                    l.append(employee)
    return l


# Step G
def make_edge_tl():
    '''Check Edge is TL or not if not make him TL.'''
    company["Anne"]["will"]["memb"]["Edge"]["POST"] = "TL"


project_manager = input("enter Project Manager name: ")
print("")
print("All employees: under {}".format(project_manager), all_employee(project_manager))
print("")
print("Employee experience more than 4 :", exp_more_than_4())
print("")
change_exp()
print("")
print("TL Name with Their Experience ", tl_exp())
print("")
smith_remove()
print("Employee experience less than 2 :", check_experience())
make_edge_tl()
