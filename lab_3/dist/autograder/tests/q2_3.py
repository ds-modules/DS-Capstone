test = {   'name': 'q2_3',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> len(Y_hat) == defaults.shape[0]\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> 22000 <= multi_rmse <= 23000\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> np.random.seed(1234);\n'
                                               '>>> expected = np.array([131575.00462172,  26777.22647566,   2573.18036936,   2824.68190761, 50299.39627643]);\n'
                                               '>>> actual = np.random.choice(Y_hat, 5);\n'
                                               '>>> np.allclose(expected, actual)\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False},
                                   {'code': '>>> np.isclose(multi_rmse, 22561.189743524323)\nTrue', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
