# write your code here
import sys

msg = [
    "Enter an equation",
    "Do you even know what numbers are? Stay focused!",
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    "Yeah... division by zero. Smart move...",
    "Do you want to store the result? (y / n):",
    "Do you want to continue calculations? (y / n):",
    " ... lazy",
    " ... very lazy",
    " ... very, very lazy",
    "You are",
    "Are you sure? It is only one digit! (y / n)",
    "Don't be silly! It's just one number! Add to the memory? (y / n)",
    "Last chance! Do you really want to embarrass yourself? (y / n)"
]

number1: float
number2: float
oper: str
result: float
mem: float = 0


def greet():
    global number1, number2, oper

    print(msg[0])
    inp = input()
    [number1, oper, number2] = inp.split()

    check_memory()


def check_memory():
    global number1, number2, mem

    if number1 == "M":
        number1 = mem
    if number2 == "M":
        number2 = mem
    check_if_number()


def check_if_number():
    global number1, number2

    try:
        number1 = float(number1)
        number2 = float(number2)
    except ValueError:
        print(msg[1])
        greet()
    else:
        check_oper()


def check_oper():
    global oper

    if oper not in ["+", "-", "*", "/"]:
        print(msg[2])
        greet()
    else:
        check_laziness(number1, number2, oper)
        do_calculation()


def check_laziness(n1: float, n2: float, op: str):
    pmsg: str = ""
    if is_one_digit(n1) and is_one_digit(n2):
        pmsg += msg[6]
    if n1 == 1 or n2 == 1 and op == "*":
        pmsg += msg[7]
    if n1 == 0 or n2 == 0 and (op == "*" or op == "+" or op == "-"):
        pmsg += msg[8]
    if pmsg != "":
        pmsg = msg[9] + pmsg
        print(pmsg)


def is_one_digit(v: float) -> bool:
    return -10 < v < 10 and v.is_integer()


def do_calculation():
    global number1, number2, oper, result

    if oper not in ["+", "-", "*", "/"]:
        print(msg[2])
        greet()
    else:
        if oper == "+":
            result = number1 + number2
        elif oper == "-":
            result = number1 - number2
        elif oper == "*":
            result = number1 * number2
        else:
            if oper == "/" and number2 == 0:
                print(msg[3])
                greet()
            elif oper == "/" and number2 != 0:
                result = number1 / number2
        print(result)
        do_storing()


def do_storing():
    print(msg[4])
    answer = input()
    if answer == "y":
        save_to_mem()
        do_continue_calc()
    elif answer == "n":
        do_continue_calc()
    else:
        do_storing()


def save_to_mem():
    global mem, result

    msg_index: int = 0
    if is_one_digit(result):
        msg_index = 10
        while not ask_to_store(msg_index):
            msg_index += 1
        mem = result
        do_continue_calc()
    else:
        mem = result
        do_continue_calc()


def ask_to_store(idx: int) -> bool:
    print(msg[idx])
    answer = input()
    can_save: bool = True

    if answer == "y":
        if idx < 12:
            return not can_save
        else:
            return can_save
    elif answer == "n":
        do_continue_calc()
    else:
        ask_to_store(idx)


def do_continue_calc():
    print(msg[5])

    answer = input()
    if answer == "y":
        greet()
    elif answer == "n":
        sys.exit()
    else:
        do_continue_calc()


greet()
