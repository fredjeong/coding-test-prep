T = int(input())

for test_case in range(1, T+1):
    n, calories_limit = map(int, input().split())

    max_score = 0
    ingredients = []
    for _ in range(n):
        ingredients.append(list(map(int, input().split())))

    def dfs(cur_node, total_score, total_calories):
        global max_score
        
        if total_calories > calories_limit:
            return

        max_score = max(max_score, total_score)

        for new_node in range(cur_node+1, n):
            new_node_score, new_node_calories = ingredients[new_node]
            dfs(new_node, total_score + new_node_score, total_calories + new_node_calories)

    for cur_node in range(n):
        cur_node_score, cur_node_calories = ingredients[cur_node]
        dfs(cur_node, cur_node_score, cur_node_calories)

    print(f"#{test_case} {max_score}")