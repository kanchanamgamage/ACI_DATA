# Extracting Data from APIC GUI

Extract Data from APIC GUI.

Sometimes we are facing dificulties to extract data from APIC GUI eventhough all the details are visible.
Example, 

![image](https://github.com/kanchanamgamage/ACI_DATA/assets/45864789/727a5a98-ecf0-4386-b875-aabc4e4ccd03)

There are fewa ways to extract data from APIC, in this article we are discussiong about moquery + python.

Step 1
Identyfy the correct moquery.
To identify the correct class you can use Opject Store inbiuld function.
first locate the data you want to extract from GUI

Figure 1.1
![image](https://github.com/kanchanamgamage/ACI_DATA/assets/45864789/859c5432-d4fa-4f43-ac07-51962a97e299)

try to enable Open in Object Store Browser Option.
If you couldnt see the oprion is enabled, try to drill donwn more 1.2 and 1.3

Figure 1.2
![image](https://github.com/kanchanamgamage/ACI_DATA/assets/45864789/f7f14998-23ce-4cfc-8c96-927c8b8e6496)


Figure 1.3

![image](https://github.com/kanchanamgamage/ACI_DATA/assets/45864789/64017dd0-498a-4396-be7a-891ce990043d)


Step 2

Login to Object Stroe

figure 2.1
![image](https://github.com/kanchanamgamage/ACI_DATA/assets/45864789/6065bdd7-9900-4c79-8495-aa0405d0cef1)

Find the Class

Figure 2.2
![image](https://github.com/kanchanamgamage/ACI_DATA/assets/45864789/202532bb-97c9-4f07-8dd3-d19084396f2f)


Step 3

Login to bash of APIC controller through SSH

![image](https://github.com/kanchanamgamage/ACI_DATA/assets/45864789/f1769200-517a-4f82-a28e-2daee54de37b)



Step 4

Excecute moquery with identified class

figure 4.1
![image](https://github.com/kanchanamgamage/ACI_DATA/assets/45864789/522d0792-441f-46e6-915e-928b29121414)

BASH is very powerfull and it has own table output, if your data set is simple try below command to get the table view

Figure 4.2
![image](https://github.com/kanchanamgamage/ACI_DATA/assets/45864789/bb39243c-bd41-41d2-9ff5-61559b3759ad)



Step 5

Now you have the data you were looking in very structured way.
you can write small python code to exctrat data into csv format.

![image](https://github.com/kanchanamgamage/ACI_DATA/assets/45864789/74b57ba6-dc9c-472d-a661-807e437957b8)




