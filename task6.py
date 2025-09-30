def greedy_algorithm(items, budget):
    ratio_items = []
    for name, data in items.items():
        ratio = data["calories"] / data["cost"]
        ratio_items.append((name, data["cost"], data["calories"], ratio))
    
    ratio_items.sort(key=lambda x: x[3], reverse=True)
    
    selected = []
    total_cost = 0
    total_calories = 0
    
    for name, cost, calories, ratio in ratio_items:
        if total_cost + cost <= budget:
            selected.append(name)
            total_cost += cost
            total_calories += calories
    
    return selected, total_cost, total_calories


def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        name, data = item_list[i - 1]
        cost = data["cost"]
        calories = data["calories"]
        
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-cost] + calories)
            else:
                dp[i][w] = dp[i-1][w]
    
    selected = []
    w = budget
    total_calories = dp[n][budget]
    total_cost = 0
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            name, data = item_list[i - 1]
            selected.append(name)
            total_cost += data["cost"]
            w -= data["cost"]
    
    return selected, total_cost, total_calories


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

print("Жадібні")
greedy_result = greedy_algorithm(items, budget)
print(f"страви {greedy_result[0]}")
print(f"вартість {greedy_result[1]}, калорійність {greedy_result[2]}")

print("\nдинамічне")
dp_result = dynamic_programming(items, budget)
print(f"страви {dp_result[0]}")
print(f"вартість {dp_result[1]}, калорійність {dp_result[2]}")