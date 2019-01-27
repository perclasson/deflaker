========
DeFlaker
========

Automatically detect flaky tests without rerunning. Inspired by https://github.com/gmu-swe/deflaker

* Free software: MIT license
* Documentation: https://deflaker.readthedocs.io.

How to develop and install
--------

Create an virtualenv

     virtualenv -p python3 venv
     pip install -r requirements_dev.txt


How to run
--------

    python -m deflaker.cli --repo=. --tests=flaky_example/ --sha=065759decaf6777b3d6f3d9adbb40ae2fe0a7764..ff7662922027159bd1b2821508f07eb8a5b499d4

Will output:

    > flaky_example/currency_test.py::TestCurrency::()::test_with_date