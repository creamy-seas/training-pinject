# Pinject Basic Template #

This is a simple [pinject](https://github.com/google/pinject) project template showcasing:
- A basic project structure with dependency injection to **custom-classes**, **custom-config-files** and **3rd party libraries**
- Please see [**Confluence page on pinject**](https://dreamsai.atlassian.net/wiki/spaces/CD/pages/51806219/Pinject) for a diagram and thorough explanation of how it works
- Please see [this folder](https://drive.google.com/drive/u/0/folders/1pyOLMyfwYCrm6LWFglNalZDZ25fue9lR) for the supplementary diagrams

![pinject_diagramg](https://drive.google.com/uc?export=view&id=1oUh8p8bVmRwuXtNlznkWG0Ak_192M_KN)


## Running: ##

All of the python code builds into a single **entrypoint**, which is called `app` in the following snippets. To build the `app` run

``` python-console
from app_builder import AppBuilder
app = AppBuilder.build('Some kind of init details')
```

after which you will have access to all of the methods that were defined in [app_manager.py](./app_manager.py):

``` python-console
app.run_print_process('Industrial Revolution has been a disaster for the hooman race')
app.run_print_process_with_init()
app.run_print_process_with_delay('Prints with a delay of three seconds', 3)
app.run_print_process_with_config()
app.run_example_pandas()
```

## Tests: ##
In terminal run nosetests in the root directory
```bash
nosetests
```

## Linting: ##
Run `pylint` to ensure that project follows [google python style guide](https://google.github.io/styleguide/pyguide.html)
```bash
pylint app
```
