# Yunis Nabiyev
# 2/3/25
# Python Homework 1 Continued
# Section 04

def main():
    print("8. An aircraft emergency locator transmitter (ELT) is a device designed to transmit a signal in the case of a crash. The Altigauge Manufacturing Company makes 80% of the ELTs, the Bryant Company makes 15% of them, and the Chartair Company makes the other 5%. The ELTs made by Altigauge have a 4% rate of defects, the Bryant ELTs have a 6% rate of defects, and the Chartair ELTs have a 9% rate of defects (which helps to explain why Chartair has the lowest market share).")
    print("a. If an ELT is randomly selected from the general population of all ELTs, find the probability that it was made by the Altigauge Manufacturing Company.")
    print("b. If a randomly selected ELT is then tested and is found to be defective, find the probability that it was made by the Altigauge Manufacturing Company.")
    print()

    print("Definitions: ")
    print("P(a): Likelihood of ELT being from Altigauge Manufacturing Company")
    print("P(b): Likelihood of ELT being from Bryant Company")
    print("P(c): Likelihood of ELT being from Chartair Company")
    print("P(d): Likelihood of defect")
    print("P(d/a): Likelihood of defect given ELT is from Altigauge Manufacturing Company")
    print("P(d/b): Likelihood of defect given ELT is from Bryant Company")
    print("P(d/c): Likelihood of defect given ELT is from Chartair Company")
    print("P(a/d): Likelihood of ELT being from Altigauge given it’s defective")
    print()

    print("Variables: ")
    p_a = 0.8
    print(f"P(a) = {p_a}")
    p_b = 0.15
    print(f"P(b) = {p_b}")
    p_c = 0.05
    print(f"P(c) = {p_c}")
    p_d_a = 0.04
    print(f"P(d/a) = {p_d_a}")
    p_d_b = 0.06
    print(f"P(d/b) = {p_d_b}")
    p_d_c = 0.09
    print(f"P(d/c) = {p_d_c}")
    print()

    print("Formula for P(a/d):")
    print("P(a/d) = (P(d/a) x P(a))/P(d)")
    print()

    print("Find P(d):")
    p_d = (p_d_a * p_a) + (p_d_b * p_b) + (p_d_c * p_c)
    print("P(d) = P(d/a) x P(a) + P(d/b) x P(b) + P(d/c) * P(c) =", f"{p_d_a} x {p_a} + {p_d_b} x {p_b} + {p_d_c} x {p_c} = {p_d}")
    print()

    print("Calculate P(a/d):")
    p_a_d = (p_d_a * p_a) / p_d
    print(f"P(a/d) = ({p_d_a} x {p_a})/{p_d} = {p_a_d}")
    print()

if __name__ == "__main__":
    main()