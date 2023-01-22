# Documentation
## Overview

md.application component provides kernel for python application.

## Architecture overview

[![Architecture overview][architecture-overview]][architecture-overview]

## Installation

```sh
pip install md.application --index-url https://source.md.land/python/
```

## Usage example

```python3
#!/usr/bin/env python3

import os
import md.application


if __name__ == '__main__':
    root_directory = os.path.abspath('..')
    
    kernel = md.application.Kernel(
        environment=md.application.ENV_DEV,
        root_directory=root_directory,
        configuration_directory=root_directory + '/etc',
        cache_directory=root_directory  + '/var/cache',
    )

    # ...
```

[architecture-overview]: _static/architecture.class-diagram.png
