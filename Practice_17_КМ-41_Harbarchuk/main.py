from factorial.factorial import fact
from exp_root.exponentiation import exp2, exp3
from exp_root.root import root2, root3
from logarithm.logarithm import log, ln, lg

def main():
    while True:
        print("\nmenu:")
        print("1. factorial")
        print("2. exponentiation (**2 and **3)")
        print("3. root (**(1/2) and **1(1/3))")
        print("4. legarithm (log, ln, lg)")
        print("5. exit")
        
        choice = input("choose an option (1-5): ")
        
        if choice == "1":
            while True:
                try:
                    n = int(input("enter a 0 or natural number: "))
                    if n < 0:
                        raise ValueError("the number must be positive or 0.")
                    print("factorial:", fact(n))
                    break
                except ValueError as e:
                    print("error:", e)
        
        elif choice == "2":
            while True:
                try:
                    x = float(input("enter number: "))
                    print("Square of the number:", exp2(x))
                    print("Cube of the number", exp3(x))
                    break
                except ValueError:
                    print("error. try again")
        
        elif choice == "3":
            while True:
                try:
                    x = float(input("enter positive number: "))
                    if x < 0:
                        raise ValueError("number must be positive.")
                    print("Square root:", root2(x))
                    break
                except ValueError as e:
                    print("error:", e)
                
            while True:
                try:
                    y = float(input("enter number: "))
                    print("Cube root:", root3(y))
                    break
                except ValueError as e:
                    print("error:", e)
        
        elif choice == "4":
            while True:
                print("\n1. Logarithm with base")
                print("2. Natural logarithm (ln)")
                print("3. Base-10 logarithm (lg)")
                log_choice = input("choose an option (1-3): ")
                
                if log_choice == "1":
                    while True:
                        try:
                            a = float(input("enter base (a > 0, a != 1): "))
                            b = float(input("enter number (b > 0): "))
                            if a <= 0 or a == 1 or b <= 0:
                                raise ValueError("The base must be greater than 0 and not equal to 1, and the number must be greater than 0.")
                            print("logarithm:", log(a, b))
                            break
                        except ValueError as e:
                            print("error:", e)

                    break
                
                elif log_choice == "2":
                    while True:    
                        try:
                            b = float(input("Enter the number (b > 0): "))
                            if b <= 0:
                                raise ValueError("The number must be greater than 0.")
                            print("Natural logarithm:", ln(b))
                            break
                        except ValueError as e:
                            print("Error:", e)

                    break
                
                elif log_choice == "3":
                    while True:
                        try:
                            b = float(input("Enter the number (b > 0): "))
                            if b <= 0:
                                raise ValueError("The number must be greater than 0.")
                            print("Base-10 logarithm:", lg(b))
                            break
                        except ValueError as e:
                            print("Error:", e)
                
                    break

                else:
                    print("Invalid option! Please try again.")
        
        elif choice == "5":
            break
        
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()