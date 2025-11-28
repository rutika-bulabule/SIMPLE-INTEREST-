import sys

if len(sys.argv) < 4:
    print("Usage: python journal_program5.py <P> <R> <T>")
    sys.exit(1)

P = float(sys.argv[1])
R = float(sys.argv[2])
T = float(sys.argv[3])
SI = (P * R * T) / 100
print("Simple Interest:", SI)