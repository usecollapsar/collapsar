from typing import Callable, Any, List, Union

class Field:
    # Attributes
    name: str
    attribute: str
    value: Any
    displayCallback: Callable
    resolveCallback: Callable
    fillCallback: Callable
    computedCallback: Callable
    defaultCallback: Callable
    rules: List[str]
    creationRules: List[str]
    updateRules: List[str]
    sortable: bool
    nullable: bool
    nullValues: List[str]
    pivot: bool
    textAlign: str
    stacked: bool
    customComponents: List[Any]
    readonlyCallback: Callable
    requiredCallback: Callable
    help_text: str = ''
    resource: Any
    nullable: bool = False

    def __init__(self, name: str, attribute: Union[str, Callable] = None, resolveCallback: Callable = None):
        self.name = name
        self.resolveCallback = resolveCallback

        self.default(None)

        if callable(attribute):
            self.computedCallback = attribute
            self.attribute = 'ComputedField'
        else:
            self.attribute = attribute if attribute is not None else name.lower().replace(' ', '_')

    def default(self, value: Any):
        # You'll have to define this function to set a default value
        pass

    def stacked(self, stack: bool = True):
        self.stacked = stack
        return self
    
    def sortable(self, sortable: bool = True):
        self.sortable = sortable
        return self
    
    def display_callback(self, callback: Callable):
        self.displayCallback = callback
        return self
    
    def get_value(self):
        return self.value
    
    def is_readonly(self):
        return False
    
    def is_required(self):
        return False
    
    def get_value(self):
        return self.value
    
    def json_serialize(self):
        return {
            'attribute': self.attribute,
            'help_text': self.help_text,
            'index_name': self.name,
            'name': self.name,
            'nullable': self.nullable,
            # 'panel': self.panel,
            # 'prefixComponent': self.
            'readonly': self.is_readonly(),
            'required': self.is_required(),
            'sortable': self.sortable,
            # 'sortableUriKey': self.sortableUriKey(),
            'stacked': self.stacked,
            # 'textAlign': self.textAlign,
            # 'validationKey': self.validationKey(),
            'value': self.get_value(),
        }