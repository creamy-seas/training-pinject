# Title of project #

### Running: ###


### Tests: ###

Make sure tests run successfully before commiting, CI will soon be set up to do this.
```bash
nosetests
```
(nosetests looks in setup.cfg for config options)

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
