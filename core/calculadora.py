import importlib
import os

class Calculadora:
    def __init__(self):
        self.operations = {
            "soma": lambda a, b: a + b,
            "subtracao": lambda a, b: a - b
        }

    def load_plugins(self, plugin_names):
        for name in plugin_names:
            module = importlib.import_module(f"plugins.{name}")
            self.operations[module.name] = module.execute
            print(f"Plugin carregado: {module.name}")

    def calculate(self, operation, a, b):
        func = self.operations.get(operation)
        return func(a, b)
