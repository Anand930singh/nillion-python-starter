from nada_dsl import *

def nada_main():
    # Define the parties involved
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    # Define the secret integers as inputs from party1
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    
    # Define another secret integer as input from party2
    my_int3 = SecretInteger(Input(name="my_int3", party=party2))

    # Perform addition of my_int1 and my_int2
    sum_result = my_int1 + my_int2

    # Perform multiplication of the sum_result and my_int3
    mul_result = sum_result * my_int3

    # Perform a conditional check: if my_int1 > my_int2
    condition_result = If(my_int1 > my_int2, my_int1 - my_int2, my_int2 - my_int1)

    # Return the results as outputs
    return [
        Output(sum_result, "sum_output", party1),
        Output(mul_result, "mul_output", party2),
        Output(condition_result, "conditional_output", party1)
    ]

# Execute the NaDa program
nada_main()
