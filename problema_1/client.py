import requests

URL = "http://localhost:5000/payment"

def main():
    N = 20  # número de chamadas

    costs = []
    expressions = []

    for i in range(N):
        res = requests.get(URL).json()

        costs.append(res["total_cost"])
        expressions.append(res["expression"])

        print(f"{i+1}: {res['expression']} = {res['total_cost']}")

    print("\n--- Resumo ---")
    print(f"Custos coletados: {costs}")


if __name__ == "__main__":
    main()
