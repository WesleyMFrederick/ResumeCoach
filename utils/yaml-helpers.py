import yaml
import re

class PreserveMarkdownLoader(yaml.SafeLoader):
    """
    Custom YAML loader that preserves Markdown formatting.
    """
    pass

class PreserveMarkdownDumper(yaml.SafeDumper):
    """
    Custom YAML dumper that preserves Markdown formatting in strings.
    """
    def represent_scalar(self, tag, value, style=None):
        # Use literal block style (|) for long strings or strings with markdown formatting
        if len(value) > 80 or re.search(r'\*\*|\*|__|_|`', value):
            style = '|'
        return super().represent_scalar(tag, value, style)

class ReadableDumper(yaml.SafeDumper):
    """
    Custom YAML dumper that prioritizes readability over preserving formatting.
    """
    def represent_scalar(self, tag, value, style=None):
        # Never use literal block style
        return super().represent_scalar(tag, value, None)

def format_yaml_with_markdown(data):
    """
    Format YAML data preserving Markdown formatting.
    
    Args:
        data: The data structure to dump as YAML
        
    Returns:
        str: YAML string with preserved Markdown formatting
    """
    return yaml.dump(
        data, 
        Dumper=PreserveMarkdownDumper,
        default_flow_style=False,
        allow_unicode=True
    )

def format_yaml_readable(data):
    """
    Format YAML data optimized for human readability.
    Does not use literal block style (|) which makes it easier to read.
    
    Args:
        data: The data structure to dump as YAML
        
    Returns:
        str: YAML string optimized for readability
    """
    return yaml.dump(
        data,
        Dumper=ReadableDumper,
        default_flow_style=False,
        allow_unicode=True,
        width=120  # Wider line width for better readability
    )