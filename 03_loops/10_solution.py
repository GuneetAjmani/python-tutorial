import time

wait=1
max_retries=5
attempt=0

while attempt < max_retries:
    print(f"Attempt : {attempt +1} , Wait Time: {wait} ")
    time.sleep(wait)
    attempt+=1
    wait*=2
    