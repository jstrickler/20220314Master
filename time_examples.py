import time


start = time.time()

for i in range(5):
    print("waiting...")
    time.sleep(.5)

end = time.time()

# time.sleep(300)

print("Done.")
elapsed = end - start
print(f"loop took {elapsed} seconds")
print(start, end)
