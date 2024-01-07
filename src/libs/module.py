from importlib import import_module

from sanic import Sanic


def setup_modules(app: Sanic):
    """
    Load some modules
    """
    for module_name in app.config.MODULE_NAMES:
        if "app." in module_name:
            MODULES = ["view", "interface"]

            for m in MODULES:
                if m == "view":
                    _module_name = f"{module_name}.view"
                    module = import_module(_module_name)
                    if bp := getattr(module, "bp", None):
                        app.blueprint(bp)
                elif m == "interface":
                    _module_name = f"{module_name}.interface"
                    module = import_module(_module_name)
                    Interface = getattr(module, "Interface", None)  # noqa
                    interface = Interface(model=Interface.model)
                    app.ext.dependency(interface)
        else:
            module = import_module(module_name)
            if bp := getattr(module, "bp", None):
                app.blueprint(bp)
