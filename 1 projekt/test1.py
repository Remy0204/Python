pi = 3.14159

print(pi)

print(type(pi))

print("mikkel")

int_10=10 

int_14=10

print(int(5324/32))

bob =[2,4,5,2,3,11]


bob.append(23)
print(len(bob))

print([1,2,3]==[3,2,1])


print({1,2,3}=={3,2,1})

print('STARTER MED OPGAVERNE HERUNDER:')
#starter med opgaverne her - Phyton basics


#opgave 1
print(5**5)

#opgave 2 
print(73%6)

#opgave 3 
print(123/3)
print(123%3)

#opgave 4 
s = "MDS is going virtual!"
print(s.split())

#opgave 5
thing = "light"
speed = 299792458  # m/s
print(f"The speed of {thing} is {speed:2e} m/s")

#opgave 6 
l = [10, [3, 4], [5, [100, 200, ["MDS"]], 23, 11], 1, 7]
print(l[2][1][2])

#opgaven 7
d = {
    "outer": [
        1,
        2,
        3,
        {"inner": ["this", "is", "inception", {"inner_inner": [1, 2, 3, "MDS"]}]},
    ]
}
print(d["outer"][3]["inner"][3]["inner_inner"][3])

#opgave 8 
t = (1, 2, 3, 4, 5)
t[-1] = 6
print(t[-1])
#because tuples are immutable, so therefore we can't change it

#opgave 9 
email = "tomas.beuzen@fakemail.com"


