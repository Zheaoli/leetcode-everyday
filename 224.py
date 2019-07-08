import typing


class Solution:
    operator_rule = {'+': 1, '-': 1, '*': 2, '/': 2}

    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        token = self.split(s)
        if len(token) < 3:
            return int(token[0])
        expression = self.get_polish_notation(token)
        return int(self.expression_to_value(expression))

    @staticmethod
    def split(s: str) -> typing.List[str]:
        result = []
        temp_value = []
        for item in s:
            if item in ["(", ")", "+", "-", "*", "/"]:
                if temp_value:
                    result.append("".join(temp_value))
                    temp_value = []
                result.append(item)
            else:
                temp_value.append(item)
        if temp_value:
            result.append("".join(temp_value))
        return result

    def get_polish_notation(self, x: typing.List[str]) -> typing.List[str]:
        expression = []
        operators = []
        for item in x:
            if item in ["+", "-", "*", "/"]:
                while len(operators) >= 0:
                    if len(operators) == 0:
                        operators.append(item)
                        break
                    operator = operators.pop()
                    if operator == "(" or self.operator_rule[
                            item] > self.operator_rule[operator]:
                        operators.append(operator)
                        operators.append(item)
                        break
                    else:
                        expression.append(operator)
            elif item == "(":
                operators.append(item)
            elif item == ")":
                while len(operators) > 0:
                    operator = operators.pop()
                    if operator == "(":
                        break
                    else:
                        expression.append(operator)
            else:
                expression.append(item)
        while len(operators) > 0:
            expression.append(operators.pop())
        return expression

    def expression_to_value(self, expression: typing.List[str]) -> int:
        temp_value = []
        for item in expression:
            if item in ["+", "-", "*", "/"]:
                temp1 = temp_value.pop()
                temp2 = temp_value.pop()
                temp_value.append(
                    self.calculate_sub_expression(temp2, temp1, item))
            else:
                temp_value.append(item)

        return temp_value[0]

    @staticmethod
    def calculate_sub_expression(item1: str, item2: str, operator: str) -> int:
        if operator == "+":
            return int(item1) + int(item2)
        elif operator == "-":
            return int(item1) - int(item2)
        elif operator == "*":
            return int(item1) * int(item2)
        elif operator == "/":
            return int(int(item1) / int(item2))


s = Solution()
print(s.calculate("(1)"))
