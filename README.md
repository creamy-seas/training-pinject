# Pinject Basic Template #

This is a simple pinject project template showcasing:
- A basic project structure
- Dependency injection of both **custom-classes**, **custom-config-files** and **3rd party libraries**
- Realising a logger and decorator in the pinject framework

    > The best documentation on this topic can be found on [google's pinject github page](https://github.com/google/pinject)


### Running: ###
All of the python code builds into a single **entrypoint**, which is called `app` in the following snippets. To build the `app` run

``` python-console
from app_build import AppBuilder
app = AppBuilder.build('Some kind of init details')
```

after which you will have access to all of the methods that were defined in [app_manager.py](./app_manager.py):

``` python-console
app.run_print_process('Industrial Revolution has been a disaster for the hooman race')
app.run_print_process_with_init()
app.run_print_process_with_delay('Prints with a delay of three seconds', 3)
app.run_print_process_with_config()
```

## Tests: ##
In terminal run nosetests in the root directory. Configurations for the test can be set in [setup.cfg](./setup.cfg)
```bash
nosetests
```

To run individual test files
```bash
python -m unittest tests.api_tests.resources_tests.accounts_resource_tests
```

## Linting: ##
Run `pylint` to ensure that project follows [google python style guide](https://google.github.io/styleguide/pyguide.html)
```bash
pylint app
```

