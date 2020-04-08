# Pinject Basic Template #

This is a simple pinject project template with examples of the following:
- basic file structure
- build an object graph
- use a library manager to bind 3rd party libraries
- parse a conf file
- instantiate a logger
- run a simple process
- run a pseudo-decorator

### Running: ###
Firstly, we have to run the classmethod to build the pinject interface and add the init_details for execution of the app

``` python-console
from app_start import AppStart
class_instance = AppStart.run('write_something')
```

Then we can run any of the commands in the app_manager:
- run_print_process(str)
- run_print_process_with_init()
- run_print_process_with_delay(str, int)
- run_print_process_with_config()

``` python-console
class_instance.run_print_process('hello')
```

### Tests: ###

Make sure tests run successfully before commiting, CI will soon be set up to do this.

In terminal run nosetests in parent directory (setup.cfg for the config options)
```bash
nosetests
```

For individual test files
```bash
python -m unittest tests.api_tests.resources_tests.accounts_resource_tests
```

### Linting: ###
```bash
pylint app
```
The above help ensure that project follows [google python style guide](https://google.github.io/styleguide/pyguide.html)

# Developing #
