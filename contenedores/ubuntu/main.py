import time

def main():
    
    while True:
        x = 0
        for i in range(100000):
            x += 1
            print(x)
        time.sleep(1)
        
if __name__ == "__main__":
    main()