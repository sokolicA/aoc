def main():
    with open("2024/day_5/input.txt") as file:
        rules = {}
        updates = []
        second_part = False
        for line in file:
            line = line.strip()
            if line == "":
                second_part=True
                continue
            if second_part:
                updates.append([int(x) for x in line.split(",")])
            else:
                rule = [int(x) for x in line.split("|")]
                if rule[0] not in rules:
                    rules[rule[0]] = {"before": set(), "after":set()}
                rules[rule[0]]["before"].add(rule[1])
                if rule[1] not in rules:
                    rules[rule[1]] = {"before": set(), "after":set()}
                rules[rule[1]]["after"].add(rule[0])
                
        
        # print(rules)
        # print(updates)

        def is_valid(update):
            for i in range(len(update)-1):
                for j in range(i+1, len(update)):
                    if update[j] in rules[update[i]]["after"]:
                        return False
            return True
        result = 0

        invalid = []
        for update in updates:
            if is_valid(update):
                result += update[len(update)//2]
            else:
                invalid.append(update)
        print("Part 1:", result)

        def correct_invalid(update):
            for i in range(len(update)-1):
                for j in range(i+1, len(update)):
                    if update[j] in rules[update[i]]["after"]:
                        tmp = update[i]
                        update[i] = update[j]
                        update[j] = tmp
                        return correct_invalid(update)
            return update[len(update)//2]
                    
        result_2 = 0
        for update in invalid:
            result_2 += correct_invalid(update)

        print("Part 2:", result_2)




if __name__=="__main__":
    main()