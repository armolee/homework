
user={'chang':[23,'18610088997','ckx123'],'aa':[11,'13520123457','ckx123']}
cond=True
while cond:
    val = input("Please enter the operation you want to execute,delete or update or find or list")
    if val=="delete":
        name=input("enter one user name")
        if user.get(name,0)!=0:
            pwd=input("Please input a password")
            if pwd==user[name][2]:
                print("Being deleted user:{}".format(name))
                user.pop(name)
            else:
                print("Incorrect password")

        else:
            print("user does not exist")
    elif val=="update":
        name = input("Please enter a username: age: contact")
        lst=name.split(':')
        if user.get(lst[0], 0) != 0:
            pwd = input("Please input a password")
            if pwd == user[lst[0]][2]:
                print("Being modified user:{}".format(name))
                user[lst[0]][1], user[lst[0]][2] = lst[0], lst[1]
            else:
                print("Incorrect password")

        else:
            print("user does not exist")
    elif val=="find":
        name = input("enter one user name")
        if user.get(name, 0) != 0:
            k=user
            k[name][2]='*'*len(k[name][2])
            print(user[name])
        else:
            print("user does not exist")
    elif val=="list":
        k = user
        for i, _ in k.items():
            k[i][2] = '*' * len(k[i][2])
        ipu=input("You can sort it through name, age, Tel")
        if ipu=="name":
            sorted(k.keys())
        elif ipu=="age":
            sorted(k.values(),key=lambda x:x[0])
        elif ipu=="tel":
            sorted(k.values(), key=lambda x: x[1])
        elif ipu=="exit":
            continue
        else:
            sorted(k.keys())
        print(k)
    elif val=="exit":
        break
    else:
        print("Please enter the correct operation")