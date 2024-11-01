## Unit Test

Qualquer empresa suficientemente grande irá exigir que você saiba testar código, para evitar dores de cabeça.

É inviável usar `print` para todas as suas funções, por isto existe Test Unit, a primeira coisa é criar um módulo para isto.

Para poder executar o test no shell: `python -m unittest test_module.py`

`ìf __name__ == '__main__'`, implica que quando o módulo for executando alguma condição extra será considerada, no nosso caso permite que possamos evitar de escrever `python -m unittest test_module.py` por apenas `test_module.py`


## References
- [Python Tutorial: Unit Testing Your Code with the unittest Module](https://www.youtube.com/watch?v=6tNS--WetLI)
- [Unit Test Framework](https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug)
- [if _ _ name _ _ == '_ _ main _ _'](https://www.youtube.com/watch?v=sugvnHA7ElY)
  