d1={}
print(type(d1))
d1={10:20,"vivek":29,"100":'1',"book":"154700","LTE":" "}
d2={"love ":"you"}
d3={"hum":"aapke","hain":"kaoun"}
c1=(d1,d2)
print(c1)
c2=(c1,d3)
print(c2)
t1=[1,2,3]
print(t1)
t2=["one","two","three"]
print(t2)
t3=tuple(zip(t1,t2))
print(t3)
new_dict=dict(t3)
print(len(t3))
print(t3)
print(new_dict)
new_dict2=dict.fromkeys(new_dict,100)
print(new_dict2)
print(new_dict2.get(2))
print(d3)
print(d3.items())
print(d1)
del d1[2]
print(d1)



