# Metadata
__author__ = 'https://md.land/md'
__version__ = '1.0.0'
__all__ = (
    # Metadata
    '__author__',
    '__version__',
    # Implementation
    'ENV_DEV',
    'ENV_PROD',
    'Kernel',
)


# Implementation
ENV_DEV = 'dev'
ENV_PROD = 'prod'


class Kernel:
    def __init__(
        self,
        environment: str,
        root_directory: str,
        configuration_directory: str,
        cache_directory: str,
    ) -> None:
        assert environment in (ENV_DEV, ENV_PROD)

        # Kernel parameters
        self.environment = environment
        self.root_directory = root_directory
        self.configuration_directory = configuration_directory
        self.cache_directory = cache_directory
