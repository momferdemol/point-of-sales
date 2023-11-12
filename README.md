
<pre>
  Title: Point of sales dummy system
  Author: Momfer de Mol
  Status: WIP
  Created: 12-11-2023
</pre>

# point-of-sales

A dummy point of sales system to learn writing unit tests with pytest.

Run program
```sh
$ python3 src/main.py
```

Run tests
```sh
$ pytest src/tests --cov
```

**Dependency**

Python modules used in `pyproject.toml`.

**Environment**

Project uses `.env` file to load environment variables which overwrites `/pos/settings.py`.

**Development**

Local development environment created with `devenv.nix`.