import math
from abc import *
from operator import contains


class Expression(ABC):
    @abstractmethod
    def evaluate(self, **bindings):
        pass

    @abstractmethod
    def derivative(self, var):
        pass
    @abstractmethod
    def expand(self):
        pass


class Power(Expression):
    def __init__(self, base, exponent):
        self.exponent = exponent
        self.base = base
    def derivative(self, var):
        if isinstance(self.exponent, Number):
            power_rule = Product(Number(self.exponent.number),
                                 Power(self.base, Number(self.exponent - 1)))
            return Product(self.base.derivative(var), power_rule)



class Number(Expression):
    def derivative(self, var):
        return Number(0)

    def expand(self):
        return self

    def evaluate(self, **bindings):
        return self.number

    def __init__(self, number):
        self.number = number


class Variable(Expression):
    def derivative(self, var):
        if self.symbol == var.symbol:
            return Number(1)
        else:
            return Number(0)

    def expand(self):
        return self
    def evaluate(self, **bindings):
        try:
            return bindings[self.symbol]
        except:
            raise KeyError("Variable '{}' is not bound.".format(self.symbol))

    def __init__(self, symbol):
        self.symbol = symbol


class Product(Expression):
    def derivative(self, var):
        if not contains(self.exp1, var):
            return Product(self.exp1, self.exp2.derivative(var))
        elif not contains(self.exp2, var):
            return Product(self.exp1.derivative(var), self.exp2)
        else:
            return Sum(
                Product(self.exp1.derivative(var), self.exp2),
                Product(self.exp1, self.exp2.derivative(var)))

    def expand(self):
        e1 = self.exp1.expand()
        e2 = self.exp2.expand()
        if isinstance(e1, Sum):
            return Sum(*[Product(e, e2).expand() for e in e1.exps])
        elif isinstance(e2, Sum):
            return Sum(*[Product(e, e1).expand() for e in e2.exps])
        else:
            return Product(e1, e2)

    def evaluate(self, **bindings):
        return self.exp1.evaluate(**bindings) * self.exp2.evaluate(**bindings)

    def __init__(self, exp1, exp2):
        self.exp2 = exp2
        self.exp1 = exp1


class Sum(Expression):
    def derivative(self, var):
        return Sum(*[exp.derivative(var) for exp in self.exps])

    def expand(self):
        return Sum(*[exp.expand() for exp in self.exps])

    def evaluate(self, **bindings):
        return sum([exp.evaluate(**bindings) for exp in self.exps])
    def __init__(self, *exps):
        self.exps = exps


class Function():
    def __init__(self, name):
        self.name = name


class Apply(Expression):
    def derivative(self, var):
        return Product(
            self.argument.derivative(var),
            _derivatives[self.function.name].substitute(_var, self.argument)
        )

    def expand(self):
        return Apply(self.function, self.argument.expand())

    def evaluate(self, **bindings):
        return _function_bindings[self.function.name](self.argument.evaluate(**bindings))

    def __init__(self, function, argument):
        self.function = function
        self.argument = argument


class Quotient():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator


def distinct_variables(exp):
    if isinstance(exp, Variable):
        return set(exp.symbol)
    elif isinstance(exp, Number):
        return set()
    elif isinstance(exp, Sum):
        return set().union(*[distinct_variables(exp) for exp in exp.exps])
    elif isinstance(exp, Product):
        return distinct_variables(exp.exp1).union(distinct_variables(exp.exp2))
    elif isinstance(exp, Power):
        return distinct_variables(exp.base).union(distinct_variables(exp.exponent))
    elif isinstance(exp, Apply):
        return distinct_variables(exp.argument)
    else:
        raise TypeError("Not a valid expression.")


_function_bindings = {
    "sin": math.sin,
    "cos": math.cos,
    "ln": math.log
}
_var = Variable('placeholder variable')
_derivatives = {
    "sin": Apply(Function("cos"), _var),
    "cos": Product(Number(-1), Apply(Function("sin"), _var)),
    "ln": Quotient(Number(1), _var),
    "sqrt": Quotient(Number(1), Product(Number(2), Apply(Function("sqrt"), _var)))
}
Y = Variable('y')
Z = Variable('z')
A = Variable('a')
B = Variable('b')
# print(Product(Variable("x"), Variable("y")).evaluate(x=2, y=5))
print(Sum(Variable("x"),Variable("c"),Number(1)).derivative(Variable("x")))
