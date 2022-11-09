# Identity operatör: is

x = y = [1,2,3,4]

z = [1,2,3,4]

print(x == y)
print(x == z) #-> liste içindeki elemanların karşılaştırmasını yaptık ve elemanlar aynı olduğu için true cevabını alırız

print(x is y)
print(x is z) #-> is komutuyla listelerin adreslerini karşılaştırırız ve aynı adrese sahip olmadıkları için false değerini verir bize.


# Membership Operator : in

x = ["Ahmet","Şirvan"]

print("Ahmet" in  x) #-> in komutuyla liste içinde sorulan elemanın bulunup bulunmadığı sorgulanır ve true veya false değerleri bize verilir.

