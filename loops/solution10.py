import time
password="shakti"

pause=1
retries=0
max_retries=5

while retries<max_retries:
    user_input=input("enter the password: ")

    if user_input==password:
        print("correct password")
        break
    elif user_input!=password:
        print("wait for",pause,"sec")
        time.sleep(pause)
        pause*=2  
        retries+=1
        continue
    print("wait for", pause, "sec")
    
    

while retries==max_retries:
    print("blocked")
    break

    

