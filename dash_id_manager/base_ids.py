from dataclasses import dataclass, field, replace, fields as dataclass_fields, Field
from typing import ClassVar, Type, Any
import sys
import dataclasses

class AutoInitFalseMeta(type):
    def __new__(mcs, name, bases, namespace):
        if name != 'BaseIDs' and any(issubclass(base, BaseIDs) for base in bases):
            annotations = namespace.get('__annotations__', {})
            for fname, ftype in annotations.items():
                if not fname.startswith('_'):
                    orig_field = namespace.get(fname, None)
                    if isinstance(orig_field, Field):
                        namespace[fname] = replace(orig_field, init=False)
                    else:
                        namespace[fname] = field(default=orig_field, init=False)
        return super().__new__(mcs, name, bases, namespace)


@dataclass(frozen=True)
class BaseIDs(metaclass=AutoInitFalseMeta):
    _prefix: ClassVar[str]

    def __post_init__(self):
        prefixes = []
        for cls in reversed(self.__class__.__mro__):
            if hasattr(cls, '_prefix'):
                prefixes.append(getattr(cls, '_prefix'))

        concatenated_prefix = '-'.join(prefixes)

        for f in dataclass_fields(self):
            if not f.name.startswith("_"):
                if f.default is not None:
                    object.__setattr__(self, f.name, f"{concatenated_prefix}-{f.default}")
                else:
                    formatted_field_name = f.name.replace('_', '-')
                    object.__setattr__(self, f.name, f"{concatenated_prefix}-{formatted_field_name}")