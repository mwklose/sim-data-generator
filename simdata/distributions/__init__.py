import importlib
import pkgutil
from typing import Dict

from distributions.distribution import Distribution

_distribution_classes: Dict[str, Distribution] = {}

def register_distribution(cls): 
    _distribution_classes[cls.__name__] = cls
    return cls

def get_distribution(distribution_cls: str, **kwargs) -> Distribution: 
    if not distribution_cls in _distribution_classes:
        raise Exception(f"[Distributions] Could not find distribution {distribution_cls} in registered distributions {list(_distribution_classes.keys())}")

    return _distribution_classes[distribution_cls].construct(**kwargs)



import pkgutil
import importlib
from pathlib import Path

prefix = "distribution_"
package_dir: Path = Path(__file__).resolve().parent

for module in pkgutil.iter_modules([str(package_dir)]):
    if not module.name.startswith(prefix): 
        continue
    mod = importlib.import_module(name=f".{module.name}", package=__package__)
