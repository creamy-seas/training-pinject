import pinject
from app.utils.library_providers.config_parser.config_parser_wrapper import ConfigParserWrapper

class ConfigParserBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('config_parser', to_class=ConfigParserWrapper)